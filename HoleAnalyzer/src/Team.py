
class Team:
    
    def __init__(self, team_name: str):
        self.team_name: str = team_name
        self.game_count = 0
        self.game_with_hole = 0
        self.game_with_clash = 0
        self.step_count = 0
        self.hole_count = 0
        self.clash_count = 0
        self.hole_steps = {}
        self.clash_steps = {}
        self.games = []

    def __str__(self):
        holes_step = ''
        for k in self.hole_steps.keys():
            holes_step += k
            holes_step += ':['
            for v in self.hole_steps[k]:
                holes_step += v
                holes_step += ', '
            holes_step += '], '
        clashes_step = ''
        for k in self.clash_steps.keys():
            clashes_step += k
            clashes_step += ':['
            for v in self.clash_steps[k]:
                clashes_step += v
                clashes_step += ', '
            clashes_step += '], '
        r = f'''######
        team_name: {self.team_name}
        game_count: {self.game_count}
        game_with_hole: {self.game_with_hole}
        game_with_clash: {self.game_with_clash}
        step_count: {self.step_count}
        hole_count: {self.hole_count}
        clash_count: {self.clash_count}
        hole_game: {self.hole_steps.keys()}
        clash_game: {self.clash_steps.keys()}
        '''
        r += f'''
        hole_game: {holes_step}
        clash_game: {clashes_step}
        '''
        return r
