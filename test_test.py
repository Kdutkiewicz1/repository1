class Client:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __hash__(self):
        return hash((self.name, self.surname))

    def __eq__(self, other):
        return (self.name, self.surname) == (other.name, other.surname)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


class Account:
    def __init__(self, cash: float):
        self.cash = cash


class Bank:
    def __init__(self):
        self.clients: dict = {}

    def add_client(self, new_client: Client, cash: float):
        self.clients[new_client] = Account(cash)

    def remove_client(self, old_client: Client):
        del self.clients[old_client]

    def add_cash(self, client: Client, cash_to_add: float):
        self.clients[client].cash += cash_to_add

    def remove_cash(self, client: Client, cash_to_remove: float):
        if self.clients[client].cash < cash_to_remove:
            print("Not enough cash to remove\n")
        else:
            self.clients[client].cash -= cash_to_remove

    def transfer_money(self, client_from, client_to, cash_to_transfer):
        if self.clients[client_from].cash < cash_to_transfer:
            print("Not enough cash to transfer\n")
        else:
            self.clients[client_from].cash -= cash_to_transfer
            self.clients[client_to].cash += cash_to_transfer

    def check_number_of_clients(self, number=float):
        return len(self.clients)

    def show_client(self, client: Client):
        return self.clients[client]

    def __str__(self):
        result = ""
        for client, account in self.clients.items():
            result += ("{} {}: {}\n".format(client.surname, client.name, account.cash))
        return result


if __name__ == '__main__':
    bank = Bank()
    marek_nowak = Client("Marek", "Nowak")
    weronika_kowalska = Client("Weronika", "Kowalska")
    agnieszka_kowalska = Client("Agnieszka", "Kowalska")
    kamil_dutkiewicz = Client("Kamil", "Dutkiewicz")

    bank.add_client(marek_nowak, cash=2000)
    bank.add_client(weronika_kowalska, cash=2000)
    bank.add_client(agnieszka_kowalska, cash=2000)
    bank.add_cash(marek_nowak, cash_to_add=1000)
    bank.remove_cash(weronika_kowalska, cash_to_remove=100)
    bank.transfer_money(client_from=agnieszka_kowalska, client_to=marek_nowak, cash_to_transfer=100)

    print(bank)

    bank_2 = Bank()
    anna_nowak = Client("Anna", "Nowak")
    bank_2.add_client(anna_nowak, cash=2000)
    print(bank_2)
    
    
    import unittest


class Test_bank(unittest.TestCase):
    def setUp(self):
        self.test_bank = Bank()
        self.marek_nowak = Client("Marek", "Nowak")
        self.weronika_kowalska = Client("Weronika", "Kowalska")
        self.agnieszka_kowalska = Client("Agnieszka", "Kowalska")
        self.kamil_dutkiewicz = Client("Kamil", "Dutkiewicz")
        self.jan_matejko = Client("Jan", "Matejko")
        self.test_bank.add_client(marek_nowak, cash=2000)
        self.test_bank.add_client(weronika_kowalska, cash=2000)

    def test_add_client(self):
        self.test_bank.add_client(self.agnieszka_kowalska, cash=3000)
        self.assertEqual(self.test_bank.clients[self.agnieszka_kowalska].cash, 3000)

    def test_remove(self):
        self.test_bank.remove_cash(self.marek_nowak, cash_to_remove=200)
        self.assertEqual(self.test_bank.clients[self.marek_nowak].cash, 1800)

    def test_transfer_money(self):
        self.test_bank.transfer_money(client_from=self.weronika_kowalska, client_to=self.marek_nowak, cash_to_transfer=300)
        self.assertEqual(self.test_bank.clients[self.weronika_kowalska].cash, 1700)
        self.assertEqual(self.test_bank.clients[self.marek_nowak].cash, 2300)

    def test_add_cash(self):
        self.test_bank.add_cash(self.weronika_kowalska, cash_to_add=400)
        self.assertEqual(self.test_bank.clients[self.weronika_kowalska].cash, 2400)

    def test_remove_client(self):
        self.test_bank.remove_client(self.marek_nowak)
        self.assertTrue(self.marek_nowak not in self.test_bank.clients.keys())

    def test_check_number_of_clients(self):
        num_of_clients = self.test_bank.check_number_of_clients()
        self.test_bank.add_client(self.kamil_dutkiewicz, cash=300000)
        num_of_clients_after = self.test_bank.check_number_of_clients()
        self.assertEqual(num_of_clients_after, num_of_clients + 1)

    def test_transfer_too_much_money(self):
        self.test_bank.transfer_money(client_from=self.weronika_kowalska, client_to=self.marek_nowak, cash_to_transfer=30000)
        self.assertEqual(self.test_bank.clients[self.weronika_kowalska].cash, 2000)
        self.assertEqual(self.test_bank.clients[self.marek_nowak].cash, 2000)

    def test_too_much_to_remove(self):
        self.test_bank.remove_cash(self.marek_nowak, cash_to_remove=20000)
        self.assertEqual(self.test_bank.clients[self.marek_nowak].cash, 2000)

    def test_show_client(self):
        self.assertEqual(self.test_bank.show_client(self.marek_nowak),self.test_bank.clients[self.marek_nowak])

    def test_no_client(self):
        self.assertTrue(self.jan_matejko not in self.test_bank.clients.keys())


if __name__ == '__main__':
    unittest.main()
