local file = io.open("data/day02_data.txt", "r")
local data
if file ~= nil then
    io.input(file)
    data = io.read()
end


local seq, halfwayPoint, success
local silverCount, goldCount = 0, 0
for seqStart, seqEnd in string.gmatch(data, "(%d+)-(%d+)") do
    local s, e = tonumber(seqStart), tonumber(seqEnd)

    for i=s,e do
        seq = tostring(i)
        -- Silver solution
        halfwayPoint = #seq // 2
        if seq:sub(1, halfwayPoint) == seq:sub(halfwayPoint+1) then
            silverCount = silverCount + i
        end

        -- Gold solution
        for testLength=1, halfwayPoint do
            -- If the subsequence does not split evenly the whole seq, skip 
            if #seq % testLength ~= 0 then goto skip end
            local testSeq = seq:sub(1, testLength)
            local currentPos = 1

            success = true
            while (currentPos <= #seq) do
                if seq:sub(currentPos, currentPos+testLength-1) ~= testSeq then
                    success = false
                    break
                end
                currentPos = currentPos + testLength
            end

            if success then break end
            ::skip::
        end
        if success then
            goldCount = goldCount + i
        end
        ::skip::
    end
end

print("Silver: "..silverCount)
print("Gold: "..goldCount)