import simpy
import numpy as np

Attack_Numbers = 10

def cyber_attack(env, name):
    print(f'{name} начал кибератаку в {env.now}')
    attack_time = np.random.exponential(1/30)
    yield env.timeout(attack_time)
    print(f'{name} закончил кибератаку в {env.now}')

def scan(env, name):
    print(f'{name} начал сканирование в {env.now}')
    scan_time = np.random.exponential(1/60)
    yield env.timeout(scan_time)
    print(f'{name} закончил сканирование в {env.now}')

def analyze_data(env, name):
    print(f'{name} начал анализ данных в {env.now}')
    analysis_time = np.random.normal(1200, 100)  # изменены параметры распределения
    yield env.timeout(analysis_time)
    print(f'{name} закончил анализ данных в {env.now}')

def analyze_incident(env, name):
    print(f'{name} начал анализ киберинцидента в {env.now}')
    analysis_time = np.random.normal(1800, 300)  # изменены параметры распределения
    yield env.timeout(analysis_time)
    print(f'{name} закончил анализ киберинцидента в {env.now}')

def determine_criticality(env, name):
    print(f'{name} начал определение критичности в {env.now}')
    analysis_time = np.random.normal(60, 10)
    yield env.timeout(analysis_time)
    print(f'{name} закончил определение критичности в {env.now}')

def choose_action_plan(env, name):
    print(f'{name} начал выбор плана действий в {env.now}')
    analysis_time = np.random.normal(120, 20)
    yield env.timeout(analysis_time)
    print(f'{name} закончил выбор плана действий в {env.now}')

def implement_action_plan(env, name):
    print(f'{name} начал реализацию плана действий в {env.now}')
    analysis_time = np.random.normal(3000, 500)  # изменены параметры распределения
    yield env.timeout(analysis_time)
    print(f'{name} закончил реализацию плана действий в {env.now}')

def repeat_scan(env, name):
    print(f'{name} начал повторное сканирование в {env.now}')
    scan_time = np.random.exponential(1/60)
    yield env.timeout(scan_time)
    print(f'{name} закончил повторное сканирование в {env.now}')

env = simpy.Environment()
max_iterations = Attack_Numbers

def process(env):
    for _ in range(max_iterations):
        yield env.process(cyber_attack(env, 'Злоумышленник'))
        yield env.process(scan(env, 'Сканер'))
        yield env.process(analyze_data(env, 'Специалист'))
        if np.random.rand() < 0.5:  # Если угрозы есть
            print("Угроза обнаружена")
            yield env.process(analyze_incident(env, 'Специалист'))
            yield env.process(determine_criticality(env, 'Специалист'))
            yield env.process(choose_action_plan(env, 'Специалист'))
            yield env.process(implement_action_plan(env, 'Специалист'))
            yield env.process(repeat_scan(env, 'Сканер'))
        else:
            print("Нет угроз")
            yield env.process(scan(env, 'Сканер'))

env.process(process(env))
env.run()