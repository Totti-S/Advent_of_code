from ast import mod
from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    all_modules = [] # Contains all the sender modules except button (that is in brodcaster)
    all_signals = [] # Keeps tab on sending signal order. We treat this as a FIFO datastructure 
    class Module:
        '''Sends pulses to other Module-classes. 
        Types:
            0: Flip-flop
            1: Conjunction
            2: Broadcaster
            3: Rx
        '''
        def __init__(self, string) -> None:
            pre_name, destinations = string.split(' -> ')

            self.name = pre_name[1:]
            prefix = pre_name[0]
            if prefix == '%':
                self.memory = False
                self.type = 0
            elif prefix == "&":
                self.type = 1
                self.memory = {}
            else:
                if pre_name == 'rx':
                    # different type for the 'rx' module ensure that it dosen't do anything sending pulse
                    self.type = 3
                else: # Broadcaster - module 
                    self.type = 2
                self.name = pre_name
            
            self.destinations = destinations
        
        def find_link_module(self)->None:
            destination_modules = self.destinations.split(', ')
            self.destinations = []
            for mod in destination_modules:
                for m in all_modules:
                    if m.name == mod:
                        break
            
                self.destinations.append(m)
                if m.type == 1:
                    m.memory[self] = False

        def send_pulse(self, high_pulse:bool, sender= None) -> None:
            if self.type == 0:
                if not high_pulse:
                    self.memory = not self.memory
                    for module in self.destinations:
                        all_signals.append((self, module, self.memory))
            elif self.type == 1:
                self.memory[sender] = high_pulse
                pulse = not all(self.memory.values())
                for module in self.destinations:
                    all_signals.append((self, module, pulse))
            elif self.type == 2: 
                for module in self.destinations:
                    all_signals.append((self, module, self.memory))

        def THE_BUTTON(self)-> None:
            if self.type == 2:
                for module in self.destinations:
                    all_signals.append((self,module, False))

    for line in data:
        all_modules.append(Module(line))
    all_modules.append(Module(f'rx -> '))
    
    brodcaster = None
    for module in all_modules:
        module.find_link_module()
        if module.type == 2:
            brodcaster = module

    gold = None
    silver = 0
    button_hits = 0
    low, high = 0, 0
    while True:
        brodcaster.THE_BUTTON()
        button_hits += 1
        low +=1
        while all_signals:
            sender, reciver, pulse = all_signals.pop(0)
            if gold is None and reciver.name == 'rx' and pulse is False:
                gold = button_hits
                break
            reciver.send_pulse(pulse, sender)
            if pulse:
                high +=1
            else:
                low += 1
        if button_hits == 1000:
            silver = low * high
        if gold is not None:
            break

    print(f'silver : {silver}')
    print(f'gold : {gold}')

if __name__ == "__main__":
    main()