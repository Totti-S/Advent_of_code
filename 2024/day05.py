import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import test
from utilities.helper_funs import nums, is_sublist

def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False, has_portions=True)
    silver, gold = 0, 0

    ordering_rules, updates = data
    ordering_rules = [nums(update.split('|')) for update in ordering_rules]

    # I was like: "naaa...aint doing linked list solution. Didn't feel like it"

    # Silver solution:  In order to find out update is in wrong order is to find contradiction 
    #                   from the rules. We go update page by page and find if there is rule that
    #                   says page of the right of the current page should be before the current page 

    wrong_orders = []
    for update in updates:
        update = nums(update.split(','))
        for i, page in enumerate(update[:-1]):
            pages_to_check = update[i:]
            fail_condition = sum([(p[0] in pages_to_check) for p in ordering_rules if p[1] == page])
            if fail_condition:
                wrong_orders.append(update)
                break
        else:
            silver += update[len(update) // 2]
    print(f'{silver = }')

    # Gold solution:    And here the silver solution that finds total ordering would have helpped.
    #                   I found out that the ordering is circular, although test case didn't.
    #                   Puzzle can't have circular ordering, otherwise it dosen't work. We can from 
    #                   that imply that there must be definible "first" page from subset of ordering
    #                   rules. Rule subset is subset that has one or both of the pages from the update
    #                   list. 
    #                       1. The "first" page can't be in the "latter" part of the rules
    #                       2. Other pages must have at least one time appear at the latter part
    #                           -> If pages wouldn't, there would be ambiguity which is the first
    #                       = Find unique page list of first part of the rules, remove all indicies
    #                         that appear in the second part
    #                   This logic can be exdented to find second, third... etc. pages. Just remove
    #                   already found pages from the list. 
    #                   NOTE: If page in the subset rules dosen't apper in the update list use it still
    #                         to find pages that couple links away from the recently found update page

    for wrong in wrong_orders:
        pages_to_check = wrong.copy()

        all_relavant_rules = [rule for rule in ordering_rules if rule[0] in wrong and rule[1] in wrong]
        first_pages = [first for first, _ in all_relavant_rules]
        second_pages = [second for _, second in all_relavant_rules]

        # You could do here the last page as well, because symmetry.
        # I rather find it so that I can use 'append' 
        first = list(set(first_pages) - set(second_pages))[0]

        correct_order = [first]
        helpper = [first]
        current_page = first
        while len(correct_order) < len(wrong):
            # Find pages that appear in second part of the rule that have current page as a first part
            next_candidates = [nd for st, nd in ordering_rules if st == current_page and nd not in helpper]
            # Get rules that dictate the inner order of the candidates. Page can't be the next one 
            # if the page appers in the second part of the rule
            cant_be_next = [rule[1] for rule in ordering_rules if is_sublist(rule, next_candidates)]
            current_page = list(set(next_candidates) - set(cant_be_next))[0]

            helpper.append(current_page)
            if current_page in wrong:
                correct_order.append(current_page)

        gold += correct_order[len(correct_order) // 2]
        
    print(f'{gold = }')

if __name__ == "__main__":
    main(mode="both", data_type='')
    test(main, __file__, (143, 123))