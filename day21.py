def main():
    with open("data/day21_data.txt", "r") as f:
        data = f.readlines()

    all_monkeys = {}
    for line in data:
        monkey, job = line.strip().split(":")

        job_eval = job.strip()
        job = job_eval.split(" ")
        if len(job) > 1:
            monkey1, monkey2 = job[0], job[2]
            all_monkeys[monkey] = {
                "num" : None,
                "job_eval" : eval(f"lambda {monkey1}, {monkey2}: {job_eval}"),
                "monkey1" : monkey1,
                "monkey2" : monkey2,
            }
        else:
            all_monkeys[monkey] = {
                "num" : int(job[0]),
                "job_eval" : None,
                "monkey1" : None,
                "monkey2" : None
            }

    while True:
        for monkey, values in all_monkeys.items():
            if values["num"] is None:
                monkey1 = values["monkey1"]
                monkey2 = values["monkey2"]
                if all_monkeys[monkey1]["num"] is not None is not all_monkeys[monkey2]["num"]:
                    num1 = all_monkeys[monkey1]["num"]
                    num2 = all_monkeys[monkey2]["num"]
                    all_monkeys[monkey]["num"] = values["job_eval"](num1, num2)

        if all_monkeys["root"]["num"] is not None:
            silver = all_monkeys["root"]["num"]
            break



    print(f"Silver : {silver}")

if __name__ == "__main__":
    main()