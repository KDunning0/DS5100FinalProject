import unittest
import numpy as np
import pandas as pd
from MonteCarlo.ProjClasses import Die, Game, Analyzer

class DieTestSuite(unittest.TestCase):
    def test_01_init(self):
        self.assertRaises(TypeError, Die, 8)
    def test_02_change_weight(self):
        Num=np.array([1,2,3,4,5,6])
        new_die=Die(Num)
        self.assertRaises(IndexError, new_die.change_weight, 8, 1.5)
    def test_03_roll_die(self):
        Num=np.array([1,2,3,4,5,6])
        new_die=Die(Num)
        new_roll=new_die.roll_die(3)
        self.assertEqual(len(new_roll),3)
        self.assertIsInstance(new_roll,list)
    def test_04_show_die(self):
        Num=np.array([1,2,3,4,5,6])
        new_die=Die(Num)
        new_die_show=new_die.show_die()
        self.assertEqual(len(new_die_show),6)
        self.assertIsInstance(new_die_show,pd.DataFrame)
class GameTestSuite(unittest.TestCase):
    def test_05_init(self):
        Num=np.array([1,2,3,4,5,6])
        new_die=Die(Num)
        new_die2=Die(Num)
        dice_list=[new_die,new_die2]
        new_game=Game(dice_list)
        self.assertEqual(len(new_game.game_dice),2)
        self.assertIsInstance(new_game,Game)
    def test_06_play(self):
        Num=np.array([1,2,3,4,5,6])
        new_die=Die(Num)
        new_die2=Die(Num)
        dice_list=[new_die,new_die2]
        new_game=Game(dice_list)
        new_game.play(10)
        self.assertEqual(len(new_game.play_run),10)
        self.assertEqual(len(new_game.play_run.columns),2)
        self.assertIsInstance(new_game.play_run,pd.DataFrame)
    def test_07_nar_or_wide(self):
        Num=np.array([1,2,3,4,5,6])
        new_die=Die(Num)
        new_die2=Die(Num)
        dice_list=[new_die,new_die2]
        new_game=Game(dice_list)
        new_game.play(10)
        self.assertRaises(ValueError, new_game.narrow_or_wide, 8)
        self.assertRaises(ValueError, new_game.narrow_or_wide, "Spaghetti")
class AnalyzerTestSuite(unittest.TestCase):
    def test_08_init(self):
        self.assertRaises(ValueError, Analyzer, 8)
    def test_09_jackpot(self):
        Num=np.array([1,2,3,4,5,6])
        new_die=Die(Num)
        new_die.change_weight(1,0)
        new_die.change_weight(2,0)
        new_die.change_weight(3,0)
        new_die.change_weight(4,0)
        new_die.change_weight(5,0)
        new_die2=Die(Num)
        new_die2.change_weight(1,0)
        new_die2.change_weight(2,0)
        new_die2.change_weight(3,0)
        new_die2.change_weight(4,0)
        new_die2.change_weight(5,0)
        dice_list=[new_die,new_die2]
        new_game=Game(dice_list)
        new_game.play(10)
        new_ana=Analyzer(new_game)
        self.assertEqual(new_ana.jackpot(),10)
        self.assertIsInstance(new_ana.jackpot(),int)
    def test_10_facecount(self):
        Num=np.array([1,2,3,4,5,6])
        new_die=Die(Num)
        new_die2=Die(Num)
        dice_list=[new_die,new_die2]
        new_game=Game(dice_list)
        new_game.play(10)
        new_ana=Analyzer(new_game)
        self.assertEqual(len(new_ana.face_count()),10)
        self.assertEqual(len(new_ana.face_count().columns),6)
        self.assertIsInstance(new_ana.face_count(),pd.DataFrame)
    def test_11_combo(self):
        Num=np.array([1,2,3,4,5,6])
        new_die=Die(Num)
        new_die2=Die(Num)
        new_die3=Die(Num)
        dice_list=[new_die,new_die2,new_die3]
        new_game=Game(dice_list)
        new_game.play(10)
        new_ana=Analyzer(new_game)
        self.assertEqual(len(new_ana.combo_count().index[0]),3)
        self.assertIsInstance(new_ana.combo_count(),pd.DataFrame)
    def test_12_permu(self):
        Num=np.array([1,2,3,4,5,6])
        new_die=Die(Num)
        new_die2=Die(Num)
        new_die3=Die(Num)
        dice_list=[new_die,new_die2,new_die3]
        new_game=Game(dice_list)
        new_game.play(10)
        new_ana=Analyzer(new_game)
        self.assertEqual(len(new_ana.permute_count().index[0]),3)
        self.assertIsInstance(new_ana.permute_count(),pd.DataFrame)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)
        
        
    
    