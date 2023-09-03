from typing import List
import copy 
DEBUG = False #True
class Game:
    
    def __init__(self, rcl_path, left_team, right_team):
        self.rcl_path: str = rcl_path
        self.left_team: str = left_team
        self.right_team: str = right_team
        self.step_count: int = 0
        self.hole_count: int = 0
        self.clash_count: int = 0
        self.left_hole_step_count: int = 0
        self.left_clash_step_count: int = 0
        self.right_hole_step_count: int = 0
        self.right_clash_step_count: int = 0
        self.left_hole_steps: List[str] = []
        self.left_clash_steps: List[str] = []
        self.right_hole_steps: List[str] = []
        self.right_clash_steps: List[str] = []

    def __str__(self):
        res = f'''######
        left_team: {self.left_team}
        right_team: {self.right_team}
        step_count: {self.step_count}
        hole_count: {self.hole_count}
        clash_count: {self.clash_count}
        left_hole_step_count: {self.left_hole_step_count}
        left_clash_step_count: {self.left_clash_step_count}
        right_hole_step_count: {self.right_hole_step_count}
        right_clash_step_count: {self.right_clash_step_count}
        left_hole_steps: {len(self.left_hole_steps)}
        left_clash_steps: {len(self.left_clash_steps)}
        right_hole_steps: {len(self.right_hole_steps)}
        right_clash_steps: {len(self.right_clash_steps)}
        '''
        return res

    @staticmethod
    def read_rcl(rcl_path):
        lines = open(rcl_path, 'r').readlines()
        lines = [line.replace('\t', ' ').split(' ') for line in lines]
        left_team = ''
        right_team = ''
        for line in lines:
            if left_team != '' and right_team != '':
                break
            if str(line).find('referee') > -1:
                continue
            team = ''.join(line[2].split('_')[:-1])
            if left_team == '':
                left_team = team
                continue
            if team != left_team:
                right_team = team
        if left_team == '' or right_team == '':
            print(f'{rcl_path} does not include left({left_team}) or right({right_team}).')
            # errors.append(f'{rcl_path} does not include left({left_team}) or right({right_team}).')
            return None
            # raise Exception(f'{rcl_path} does not include left({left_team}) or right({right_team}).')
        g = Game(rcl_path, left_team, right_team)
        step = ''
        left_agents = []
        right_agents = []
        left_main_actions = []
        right_main_actions = []
        cycle = []
        steps = []
        for line in lines:
            if line[0].startswith('0') or line[0].startswith('3000') or line[0].startswith('6000') or line[0].startswith('7000'):
                continue
            if line[0].startswith('8000'):
                break
            if line[1].startswith('(referee'):
                continue
            if step != line[0]:
                cycle = 0
                if step != '':
                    steps.append({'step': step,
                                  'left': len(left_agents), 'left_set': len(set(left_agents)),
                                  'left_agents': copy.copy(left_agents),
                                  'left_actions': copy.copy(left_main_actions),
                                  'right': len(right_agents), 'right_set': len(set(right_agents)),
                                  'right_agents': copy.copy(right_agents),
                                  'right_actions': copy.copy(right_main_actions),
                                  'cycle': line[0].split(',')[0],
                                  'subcycle': line[0].split(',')[1]})
                    left_agents.clear()
                    right_agents.clear()
                    left_main_actions.clear()
                    right_main_actions.clear()
            
                step = line[0]
            team = ''.join(line[2].split('_')[:-1])
            agent = line[2].split('_')[-1]
            actions = ' '.join(line[3:])
            if agent != 'Coach' and agent != 'Coach:':
                if team == left_team:
                    left_agents.append(int(agent.replace(':', '')))
                    left_main_actions.append(actions)
                else:
                    right_agents.append(int(agent.replace(':', '')))
                    right_main_actions.append(actions)
        left_kills = {}
        for u in range(1, 12):
            for index in range(len(steps) - 1, -1, -1):
                if u in steps[index]['left_agents']:
                    left_kills[u] = index
                    break
        left_counts = {}
        for index in range(len(steps)):
            left_counts[index] = len([i for i in left_kills.values() if i >= index])

        right_kills = {}
        for u in range(1, 12):
            for index in range(len(steps) - 1, -1, -1):
                if u in steps[index]['right_agents']:
                    right_kills[u] = index
                    break
        right_counts = {}
        for index in range(len(steps)):
            right_counts[index] = len([i for i in right_kills.values() if i >= index])

        left_freeze = [[] for _ in range(11)]
        for index in range(len(steps)):
            for action, unum in zip(steps[index]['left_actions'], steps[index]['left_agents']):
                if len(left_freeze[unum-1]) > 0 and index - left_freeze[unum-1][-1] < 10:
                    continue
                if 'tackle' in action:
                    left_freeze[unum-1].append(index)
        left_may_freeze = [0 for s in steps]
        for p_t in left_freeze:
            for s in p_t:
                for i in range(s, min(s + 10, len(steps))):
                    left_may_freeze[i] += 1

        right_freeze = [[] for _ in range(11)]
        for index in range(len(steps)):
            for action, unum in zip(steps[index]['right_actions'], steps[index]['right_agents']):
                if len(right_freeze[unum - 1]) > 0 and index - right_freeze[unum - 1][-1] < 10:
                    continue
                if 'tackle' in action:
                    right_freeze[unum - 1].append(index)
        right_may_freeze = [0 for s in steps]
        for p_t in right_freeze:
            for s in p_t:
                for i in range(s, min(s + 10, len(steps))):
                    right_may_freeze[i] += 1

        g.step_count = len(steps)
        index = 0
        last_hole = -1
        while index < len(steps):
            if steps[index]['left'] == left_counts[index] and steps[index]['left_set'] == left_counts[index]:
                pass
            if steps[index]['left_set'] < left_counts[index] - left_may_freeze[index]:
                if DEBUG:
                    print('left H at S', steps[index]['cycle'], steps[index]['subcycle']) #DEBUG
                g.hole_count += 1
                g.left_hole_step_count += 1
                g.left_hole_steps.append(steps[index]['step'])
                last_hole = index
            if steps[index]['left'] > steps[index]['left_set'] and last_hole == index - 1:
                if DEBUG:
                    print('left C at S', steps[index]['cycle'], steps[index]['subcycle']) #DEBUG
                g.clash_count += 1
                g.left_clash_step_count += 1
                g.left_clash_steps.append(steps[index]['step'])
            index += 1
            continue

        index = 0
        last_hole = -1
        while index < len(steps):
            if steps[index]['right'] == right_counts[index] and steps[index]['right_set'] == right_counts[index]:
                pass
            if steps[index]['right_set'] < right_counts[index] - right_may_freeze[index]:
                if DEBUG:
                    print('right H at S', steps[index]['cycle'], steps[index]['subcycle']) #DEBUG
                g.hole_count += 1
                g.right_hole_step_count += 1
                g.right_hole_steps.append(steps[index]['step'])
                last_hole = index
            if steps[index]['right'] > steps[index]['right_set'] and last_hole == index - 1:
                if DEBUG:
                    print('right C at S', steps[index]['cycle'], steps[index]['subcycle']) #DEBUG
                g.clash_count += 1
                g.right_clash_step_count += 1
                g.right_clash_steps.append(steps[index]['step'])
            index += 1
            continue
        if DEBUG:
            print(g) #DEBUG
        return g
