local file = io.open("data/day03_data.txt", "r")
local data
if file ~= nil then
    io.input(file)
    data = io.read("*a")
    file:close()
end

local banks = {}
for w in string.gmatch(data, '([^\n]+)') do
    banks[#banks + 1] = w
end

local function max_in_string(str)
    -- Find the max value and return the earliest index
    local index = 0
    local current_index = 1
    local max = 0
    for i in string.gmatch(str, "%d") do
        local num = tonumber(i)
        if num > max then
            index = current_index
            max = num
            if max == 9 then break end
        end
        current_index = current_index + 1
    end
    return index, max
end

-- For silver solution just find two the highest numbers
local silver_count = 0
local result_number
for _, bank in pairs(banks) do
    local first, second
    local index, num = max_in_string(bank)
    if index ~= #bank then
        first = num
        _, second = max_in_string(string.sub(bank, index+1))
    else
    -- If the highest number is the last number then it's the latter number
        second = num
        _, first = max_in_string(string.sub(bank, 1, index-1))
    end
    result_number = tonumber(first..second)
    silver_count = silver_count + result_number
end

-- For Gold solution search for highest number like previously, but for each number,
-- starting from left, the search radius is limited for we the number can theorically be.
-- (e.g. if 2 length number in 3 number sequence the first number can't be at the last position)
local gold_count = 0
for _, bank in pairs(banks) do
    -- print("Seq: "..bank)
    local result_seq_string = ""
    local s_idx = 1
    local e_idx, current_index, num, index
    local discarded = 0

    while #result_seq_string ~= 12 do
        current_index = #result_seq_string + 1
        -- Generally search space is
        --      start index: order of the number (+ no. skipped numbers)
        --      end index: excess numbers + order of the number
        s_idx = current_index + discarded
        e_idx = #bank - 12 + current_index
        -- Stop there isn't nothing to search and end rest to sequence 
        if s_idx == e_idx then
            result_seq_string = result_seq_string..bank:sub(s_idx)
            break
        else
            index, num = max_in_string(bank:sub(s_idx, e_idx))
            result_seq_string = result_seq_string..num
            if index ~= 1 then
                -- First number wasn't highest, 'discarding' happend
                discarded = discarded + index - 1
            end
        end
    end
    assert(#result_seq_string == 12)
    gold_count = gold_count + tonumber(result_seq_string)
end

print("Silver: "..silver_count)
print("Gold: "..gold_count)
