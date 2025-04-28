import pandas

class BaseStep:
    _sbirky: pandas.DataFrame
    _column_name: str

    def proceed(self, Sbirky: pandas.DataFrame) -> pandas.DataFrame:
        self._sbirky = Sbirky
        return self.compute()

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: f"".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

