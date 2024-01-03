from utilities.get_data import get_data
import re
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False, has_portions=True)
    workflows, parts = data


    class Workflow:
        def __init__(self, name, conds, else_cond) -> None:
            self.name = name
            self.conds = conds
            self.else_cond = else_cond
            self.points_to_workflows = []
        
        def find_cond_names(self):
            tmp = [x[1] for x in self.conds]
            tmp.append(self.else_cond)
            return tmp

        def __str__(self):
            return f'{self.name}, [{self.points_to_workflows}]'
    
    print(data)
    all_works = []
    for wf in workflows:
        wf = wf.rstrip('}')
        name, rest_pattern = wf.split('{')
        conditions = rest_pattern.split(',')
        splitted_conds = []
        for condition in conditions[:-1]:
            tmp_cond, go_to_node = condition.split(':')
            if go_to_node == 'A':
                go_to_node = True
            elif go_to_node == 'R':
                go_to_node = False
            splitted_conds.append((tmp_cond, go_to_node))

        # The last node dosen't have condition as it can be thought as an else clause
        else_statment = conditions[-1]
        if else_statment == 'A':
            else_statment = True
        elif else_statment == 'R':
            else_statment = False
        work = Workflow(name, splitted_conds, else_statment)
        all_works.append(work)
    
    starting_workflow = None
    for work in all_works:
        if work.name == 'in':
            starting_workflow = work
            break
    # Lets try to organize this mess
    queue = [starting_workflow]
    while queue:
        work = queue.pop(0)
        names = work.find_cond_names()
        for i, name in enumerate(names):
            if type(name) != bool:
                for w in all_works:
                    if w.name == name:
                        break
                work.points_to_workflows.append(w)
                queue.append(w)
            else:
                work.points_to_workflows.append(name)

            work.else_cond = None


    all_works_all = all_works.copy()
    remove_works = []

    for work in all_works:
        for b in [True, False]:
            if all([x is b for x in work.points_to_workflows]):
                remove_works.append(work)
                for w in all_works:
                    for i, point_wf in enumerate(w.points_to_workflows):
                        if point_wf == work:
                            w.points_to_workflows[i] = b

    for w in remove_works:
        all_works.remove(w)
    
    for w in all_works:
        print(w.points_to_workflows)
    total = 0
    def rec(wf:Workflow, parts:dict)->bool:
        a = parts['a']
        m = parts['m']
        x = parts['x']
        s = parts['s']
        for i,cond in enumerate(wf.conds):
            print(cond[0], eval(cond[0]))
            if eval(cond[0]):
                if type(wf.points_to_workflows[i]) == bool:
                    return wf.points_to_workflows[i]
                else:
                    return rec(wf.points_to_workflows[i], parts)
        else:
            if type(wf.points_to_workflows[-1]) == bool:
                return wf.points_to_workflows[-1]
            else:
                return rec(wf.points_to_workflows[-1], parts)
        assert True, 'dont come here'

    for part in parts:
        part = part.replace('=','\':')
        part = part.replace(',', ',\'')
        part = part.replace('{', '{\'')
        part_dict = eval(part)
        value = rec(starting_workflow, part_dict)
        print(value)
        if value:
            total += sum(part_dict.values())
            print(part)
    
    print(f'{mode} : {total}')

if __name__ == "__main__":
    main()