# DS5100FinalProject

# Metadata

### Monte Carlo Simulator Project
### Author: Katie Dunning

# Synopsis

### Install
pip install git+https://github.com/KDunning0/DS5100FinalProject

### Class 1: Die

from MonteCarlo.ProjClasses import Die

Num=np.array([1,2,3,4,5,6])
New_Die=Die(Num)
New_Die.change_weight(5,1.5)

### Class 2: Game

from MonteCarlo.ProjClasses import Game

die_list=list(New_Die,New_Die)
New_Game=Game(die_list)
Rolls=1000
New_Game.play(1000)

### Class 3: Analyzer

from MonteCarlo.PojClasses import Analyzer

New_Ana=Analyzer(New_Game)
New_Ana.jackpot()
New_Ana.face_count()

# API Documentation

### Class 1: Die

##### Method 1: __init__(N)
Creates an instance of the die.
           input=N, a numpy array of die faces (numeric or alphabetic)
           Creates=Weights, a numpy array of uniform weights for each face
           die_frame, a pd dataframe of faces/sides and weights
           
##### Method 2: change_weight(num_face,num_weight)
Changes the weight of a single die face.
           input=num_face, a single member of self.faces.
           num_weight, integer or float to replace weight of num_face
           Changes=Alters the weight within self.die_frame

##### Method 3: roll_die(rolls=1)
Rolls the dice a set number of times.
           default=rolls, integer, rolls 1 time.
           input=rolls, integer, the number of times the die is rolled.
           returns=temp_roll_holder, list, the die face rolled for each roll
           
##### Method 4: show_die()
Shows the die object in its current state
            returns=self.die_frame, pd Dataframe, faces/sides and weights of the die

### Class 2: Game

##### Method 1: __init__(dice_list)
Creates an instance of the Game object
           input=dice_list, list, a list of already instanced Die objects with same face/side count
           creates=self.game_dice, list, originally dice_list

##### Method 2: play(roll_num)
Rolls the dice in self.game_dice a set number of times, then stores results
        input=roll_num, integer, a number of time for all dice to be rolled
        creates=self.play_run, pd DataFrame, stores the faces rolled for each die for each roll

##### Method 3: narrow_or_wide(ans)
Displays self.play_run in either wide or narrow orientation
        input=ans, string, the value 'narrow' or 'wide' depending on desired table.
        return=narrow_tab, pd DataFrame, a narrow version of self.play_run if 'narrow' is selected.
        play_run, pd DataFrame, returns play_run unchanged if 'wide' is selected.

### Class 3: Analyzer

##### Method 1: __init__(game_obj)
Creates an instance of Analyzer
        input=game_obj, an instance of class Game
        creates=self.gameobj, stores game_obj
        self.dieface, np array, stores the faces present on a die
        
##### Method 2: jackpot()
Outputs an integer with the number of rolls where all dice equal the same face.
        return=count, integer, the number of rolls where all dice equal the same face.
        
##### Method 3: face_count()
Counts the number of times all faces/sides appear in each roll of all dice
        return=fa_count, pd DataFrame, the counts for all faces for each roll of all dice

##### Method 4: combo_count()
Returns a combination count table of face rolls and the number of times occurred.
        return=row_tup_combo, pd DataFrame, the combo counts for each tuple.

##### Method 5: permute_count()
Returns a permutation count table of face rolls and the number of times occurred.
        return=row_tup_perm, pd DataFrame, the permutation counts for each tuple."""
        
