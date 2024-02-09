from wtforms import Form, FloatField


class FormulaForm(Form):
    t = FloatField("t", description="Время с начала разлива")
    p_v = FloatField("ρв", description="Плотность воды")
    p_n = FloatField("ρн", description="Плотность нефти")
    Q_0 = FloatField("Q₀", description="Объем нефтяного разлива")
    v = FloatField("ν", description="Кинематическая вязкость воды")


class ResultForm(Form):
    A_2 = FloatField("A₂", description="Площадь разлива")
    R_1 = FloatField("R₁", description="Радиус нефтяного пятна")


__all__ = [FormulaForm, ResultForm]
