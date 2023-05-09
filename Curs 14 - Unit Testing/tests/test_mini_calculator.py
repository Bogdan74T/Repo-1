from app.mini_calculator import MiniCalculator
class TestMiniCalculator:

    def setup_method(self):
        self.mini_calculator = MiniCalculator(10,5)

    def test_adunare(self):
       assert self.mini_calculator.adunare() == 15, "Adunarea nu functioneaza corect"

    def test_scadere(self):
        assert self.mini_calculator.scadere() == 5, "Scaderea nu functioneaza corect"

    def test_inmultire(self):
        assert self.mini_calculator.inmultire() == 50, "Inmultirea nu functioneaza corect"

    def test_impartire(self):
        assert self.mini_calculator.impartire() == 2, "Impartirea nu functioneaza corect"

    def test_impartire_2(self):
        self.mini_calculator = MiniCalculator(5,2)
        assert self.mini_calculator.impartire() == 2.5, "Impartirea cu virgula nu functioneaza corect"