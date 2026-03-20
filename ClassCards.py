import random
from collections import defaultdict

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    SUITS = ['♠', '♥', '♦', '♣']
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    def __init__(self, num_decks=1, include_jokers=False):
        self.cards = []
        for _ in range(num_decks):
            for suit in self.SUITS:
                for rank in self.RANKS:
                    self.cards.append(Card(suit, rank))
            if include_jokers:
                self.cards.append(Card('Joker', 'Red'))
                self.cards.append(Card('Joker', 'Black'))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop() if self.cards else None

class Game:
    def __init__(self, num_players, num_decks):
        self.num_players = num_players
        self.deck = Deck(num_decks)
        self.players = defaultdict(list)
        self.cards_distributed = 0
    
    def shuffle_deck(self):
        self.deck.shuffle()
    
    def distribute_cards(self, cards_per_player):
        for _ in range(cards_per_player):
            for player in range(1, self.num_players + 1):
                card = self.deck.deal_card()
                if card:
                    self.players[player].append(card)
                    self.cards_distributed += 1
    
    def show_results(self):
        print(f"{'='*50}")
        print(f"Cartas distribuídas: {self.cards_distributed}")
        print(f"Cartas restantes no baralho: {len(self.deck.cards)}")
        print(f"{'='*50}\n")
        
        for player in range(1, self.num_players + 1):
            cards_str = ' '.join(str(card) for card in self.players[player])
            print(f"Jogador {player}: {cards_str}")

# Uso
if __name__ == "__main__":  
    num_players = int(input("Quantos jogadores? "))
    num_decks = int(input("Quantos baralhos? "))
    include_jokers = input("Incluir coringas? (s/n) ").lower() == 's'
    cards_per_player = int(input("Quantas cartas por jogador? "))
    
    game = Game(num_players, num_decks)
    game.deck = Deck(num_decks, include_jokers)
    game.shuffle_deck()
    game.distribute_cards(cards_per_player)
    game.show_results()

 # Este código define as classes Card, Deck e Game para simular um jogo de cartas. O usuário pode especificar o número de jogadores, o número de baralhos e quantas cartas cada jogador deve receber. O programa então embaralha o baralho, distribui as cartas e exibe os resultados.

 # preciso incluir nesse projeto a opção de ter ou não coringas no baralho. Se o usuário escolher incluir coringas, cada baralho deve conter 2 coringas (um vermelho e um preto). O programa deve ajustar a distribuição de cartas e a contagem de cartas restantes no baralho de acordo com a inclusão dos coringas.
