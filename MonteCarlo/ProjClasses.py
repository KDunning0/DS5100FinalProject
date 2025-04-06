import numpy as np
import pandas as pd

class Die():
    """Creates a die object with weights that can be rolled."""
    def __init__(self,N):
        """Creates an instance of the die.
        input=N, a numpy array of die faces (numeric or alphabetic).
        Creates=Weights, a numpy array of uniform weights for each face.
        die_frame, a pd dataframe of faces/sides and weights"""
        if not isinstance(N,np.ndarray):
            raise TypeError("N must be a numpy array.")
        if len(np.unique(N)) != len(N):
            raise ValueError("Numbers must be distinct.")
        self.faces=N
        self.weights=np.array([1.0 for num in range(len(N))])
        self.die_frame=pd.DataFrame({'sides':self.faces,'weights':self.weights}).set_index('sides')
    def change_weight(self,num_face,num_weight):
        """Changes the weight of a single die face.
        input=num_face, a single member of self.faces.
        num_weight, integer or float to replace weight of num_face
        Changes=Alters the weight within self.die_frame"""
        if num_face not in self.faces:
            raise IndexError("Face not in dice faces.")
        if not isinstance(num_weight,(int,float)) and num_weight.lstrip('-').replace('.','').isdigit()==False:
            raise TypeError("Not a number and/or can't become a number.")
        new_weight=float(num_weight)
        self.die_frame.loc[num_face]=new_weight
        self.weights=np.array(self.die_frame.iloc[:,0])
    def roll_die(self,rolls=1):
        """Rolls the dice a set number of times.
        default=rolls, integer, rolls 1 time.
        input=rolls, integer, the number of times the die is rolled.
        returns=temp_roll_holder, list, the die face rolled for each roll"""
        temp_roll_holder=[]
        for i in range(rolls):
            new_roll=self.die_frame.sample(weights=self.weights).index[0]
            temp_roll_holder.append(new_roll)
        return temp_roll_holder
    def show_die(self):
        """Shows the die object in its current state
        returns=self.die_frame, pd Dataframe, faces/sides and weights of the die"""
        return self.die_frame
    
class Game():
    """Creates a Game object for rolling multiple dice with the same side/face count."""
    def __init__(self,dice_list):
        """Creates an instance of the Game object
        input=dice_list, list, a list of already instanced Die objects with same face/side count
        creates=self.game_dice, list, originally dice_list"""
        self.game_dice=dice_list
    def play(self,roll_num):
        """Rolls the dice in self.game_dice a set number of times, then stores results
        input=roll_num, integer, a number of time for all dice to be rolled
        creates=self.play_run, pd DataFrame, stores the faces rolled for each die for each roll"""
        self.play_run=pd.DataFrame()
        for i, dice in enumerate(self.game_dice):
            self.play_run[i]=pd.DataFrame(dice.roll_die(roll_num))
        self.play_run.index=range(1, len(self.play_run)+1)
        self.play_run.index.name='Roll Num'
    def narrow_or_wide(self,ans):
        """Displays self.play_run in either wide or narrow orientation
        input=ans, string, the value 'narrow' or 'wide' depending on desired table.
        return=self.narrow_tab, pd DataFrame, a narrow version of self.play_run if 'narrow' is selected.
        self.play_run, pd DataFrame, returns self.play_run unchanged if 'wide' is selected."""
        if not isinstance(ans,str):
            raise ValueError("Not a string.")
        if ans.lower() != 'narrow' and ans.lower() != 'wide':
            raise ValueError("Please enter narrow or wide.")
        if ans.lower() == 'narrow':
            self.narrow_tab=self.play_run.stack().to_frame('Outcome')
            return self.narrow_tab
        if ans.lower() == 'wide':
            return self.play_run

class Analyzer():
    """Computes the statsitics of a single Game object."""
    def __init__(self,game_obj):
        """Creates an instance of Analyzer
        input=game_obj, an instance of class Game
        creates=self.gameobj, stores game_obj
        self.dieface, np array, stores the faces present on a die"""
        if not isinstance(game_obj,Game):
            raise ValueError("Not a game object.")
        self.gameobj=game_obj
        self.dieface=game_obj.game_dice[0].faces
    def jackpot(self):
        """Outputs an integer with the number of rolls where all dice equal the same face.
        return=count, integer, the number of rolls where all dice equal the same face."""
        count=0
        for ind, row in self.gameobj.play_run.iterrows():
            if len(pd.unique(row.values))==1:
                count+=1
        return count
    def face_count(self):
        """Counts the number of times all faces/sides appear in each roll of all dice
        return=fa_count, pd DataFrame, the counts for all faces for each roll of all dice"""
        fa_count=pd.DataFrame(index=self.gameobj.play_run.index)
        for face in self.dieface:
            fa_count[face]=self.gameobj.play_run.apply(lambda r:(r==face).sum(),axis=1)
        return fa_count
    def combo_count(self):
        """Returns a combination count table of face rolls and the number of times occurred.
        return=row_tup_combo, pd DataFrame, the combo counts for each tuple."""
        row_tup=[tuple(sorted(self.gameobj.play_run.loc[i])) for i in self.gameobj.play_run.index]
        row_tup_combo=pd.DataFrame.from_dict({tuple_combo: row_tup.count(tuple_combo) for tuple_combo in set(row_tup)},orient='index')
        row_tup_combo.index.name='Combo Roll'
        row_tup_combo=row_tup_combo.rename(columns={0:'Combo Count'})
        return row_tup_combo
    def permute_count(self):
        """Returns a permutation count table of face rolls and the number of times occurred.
        return=row_tup_perm, pd DataFrame, the permutation counts for each tuple."""
        row_tup=[tuple(self.gameobj.play_run.loc[i]) for i in self.gameobj.play_run.index]
        row_tup_perm=pd.DataFrame.from_dict({tuple_perm: row_tup.count(tuple_perm) for tuple_perm in set(row_tup)},orient='index')
        row_tup_perm.index.name='Permute Roll'
        row_tup_perm=row_tup_perm.rename(columns={0:'Permute Count'})
        return row_tup_perm    


        
