
local file = io.open("data/day01_data.txt", "r")
if file == nil then
    return
end
io.input(file)

-- Both solution
-- Starting point at 50
local dial_pos = 50
local silver_count = 0
local gold_count = 0
local starting_pos, passthrough_count, direction, length

for line in io.lines() do
    direction = string.sub(line, 1, 1) == "R"
    length = tonumber(string.sub(line, 2))

    starting_pos = dial_pos
    -- This and--or works like ternary
    dial_pos = dial_pos + (direction and length or -length)

    -- Gold solutions needs to check if there are passthroughs
    passthrough_count = math.abs(dial_pos) // 100
    
    -- Count the positive -> negative to gold solution
    gold_count = gold_count + (dial_pos < 0 and starting_pos ~= 0 and 1 or 0)
    
    -- Convienently this works both directions nicely
    dial_pos = dial_pos % 100

    -- Count everytime after sequence position is exactly zero for Silver solution
    if dial_pos == 0 then
        silver_count = silver_count + 1
    end

    gold_count = gold_count + passthrough_count
    -- There is special case I did not handle, where the rule would say R0 or L0, not moving
    -- that could technically tick silver count up, but for the gold it shouldn't.
    -- My data didn't contain those so I ignore this case.
    gold_count = gold_count + (dial_pos == 0 and passthrough_count == 0 and 1 or 0)

end
print("Silver solution: "..silver_count)
print("Gold solution: "..gold_count)

file:close()
