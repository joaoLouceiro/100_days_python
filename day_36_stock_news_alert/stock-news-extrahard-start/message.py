class Message:
    def __init__(self, title, message, symbol, percent):
        self.title = title
        self.message = message
        self.symbol = symbol
        self.percent = percent

    def format(self) -> str:
        return (f"{self.symbol}: {'🔺' if self.percent > 0 else '🔻'}{round(self.percent)}%:\n"
                f"Headline: {self.title}\n"
                f"Brief: {self.message}")
