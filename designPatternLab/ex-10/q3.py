from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, base_price):
        pass

class NormalSaleStrategy(PricingStrategy):
    def calculate_price(self, base_price):
        return base_price

class FestivalSaleStrategy(PricingStrategy):
    def calculate_price(self, base_price):
        discount = base_price * 0.20
        return base_price - discount

class SaleContext:
    def __init__(self, strategy: PricingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PricingStrategy):
        self.strategy = strategy

    def calculate_final_price(self, base_price):
        return self.strategy.calculate_price(base_price)



base_price = 100
normal_sale = NormalSaleStrategy()
sale_context = SaleContext(normal_sale)
print(f"Normal Sale Price: ${sale_context.calculate_final_price(base_price)}")
festival_sale = FestivalSaleStrategy()
sale_context.set_strategy(festival_sale)
print(f"Festival Sale Price: ${sale_context.calculate_final_price(base_price)}")
