from src.simulation import run_simulation

def main() -> None:
    """
    Главный модуль запуска приложения
    """
    run_simulation(steps=6, seed=10)

if __name__ == '__main__':
    main()
