from game.scripting.action import Action


class MoveActorsAction(Action):

    def execute(self, cast, script):
        all_actors = cast.get_all_actors()
        
        # 2) loop through the actors

        for snake in (all_actors):
            # 3) call the move_next() method on each actor
            sanke.move_next()
