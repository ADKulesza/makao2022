# Strategy - definiująca zachowanie gracza; 
# zaimplementowana w niej metoda best_move(crds: List[Card], e: Effect, top: Card) 
# przyjmuje listę kart gracza, aktualny efekt gry oraz kartę na stole i zwraca kartę (karty) które ma zagrać gracz. 
# Podstawowe klasy potomne to RandomStrategy i Human

#

#stategia agressive: gracz wybiera kartę, która ma najgorszy skutek dla przeciwników
#czyli na przykład 2, 3 żeby musieli dobrac z talii
#wybiera kolejno od najgorszej skutkiemm dla przeciwników: K, 3, 2, 4, J (?)
#startegia random: g. wybiera kartę losowo spośród odpowiednich 
#strategia quick: wybieranie kart tylko pod względem jak najszybszego pozbycia się ich
#bez uwzględniania jaki przyniesie skutek dla innych graczy
#czyli będzie sprawdzać jaką kartę wybrać żeby pozbyć się np w jednym ruchu jeszcze innych kart 
#strategia dzban: zapomina wyłożyć więcej kart niż jedną, nawet, jeśli może 

from abc import abstractmethod
from Card import Card 
from Effect import Effect

class Strategy:

    def __init__(self):
        pass

    @abstractmethod
    def best_move(self, crds: List[Card], e: Effect, top_card: Card):
        return list_of_cards

class agressive(Strategy):
    def best_move(self, crds: List[Card], e: Effect, top_card: Card):
        self.crds = crds
        self.e = e
        self.top_card = top_card


