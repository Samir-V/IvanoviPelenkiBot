import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- КНОПКИ ---
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📘 Теория")],
        [KeyboardButton(text="📝 Задания")]
    ],
    resize_keyboard=True
)

theory_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📌 Все падежи")],
        [KeyboardButton(text="🟢 Именительный"), KeyboardButton(text="🔵 Родительный")],
        [KeyboardButton(text="🟡 Дательный"), KeyboardButton(text="🔴 Винительный")],
        [KeyboardButton(text="🟣 Творительный"), KeyboardButton(text="⚫ Предложный")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)

levels_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🟢 Уровень 1")],
        [KeyboardButton(text="🟡 Уровень 2")],
        [KeyboardButton(text="🔵 Уровень 3")],
        [KeyboardButton(text="🔴 Уровень 4")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)

# --- ДАННЫЕ (сокращённые, ты можешь расширить) ---
theory_text = """
📘 Что такое падеж?

Падеж — это грамматическая категория имени 
(существительного, прилагательного, числительного,
местоимения), которая показывает его синтаксическую
роль в предложении и выражает его отношение к 
другим словам в словосочетании и предложении. 
Проще говоря, падеж отвечает на вопросы и указывает, 
как слово связано с действием или другим предметом.

В русском языке 6 падежей:

Их традиционно заучивают в определенном порядке, который
часто задается мнемонической фразой: «Иван Ро-
дил Девчонку, Велел Тащить Пеленку» (Имени-
тельный, Родительный, Дательный, Винительный,
Творительный, Предложный).

1. Именительный — Кто? Что?
2. Родительный — Кого? Чего?
3. Дательный — Кому? Чему?
4. Винительный — Кого? Что?
5. Творительный — Кем? Чем?
6. Предложный — О ком? О чём?
"""

imen_text = """
🟢 Именительный падеж

Вопросы: Кто? Что?
Роль в предложении:
Подлежащее (главный действующий предмет) 
или именная часть составного сказуемого.
Характерное значение: Называние предмета, 
лица, явления. Исходная, словарная форма слова.

Пример:
(Кто?) Студент читает книгу. (Подлежащее)
Мой (кто?) брат — инженер. (Именная часть сказуемого)
Наступила осень (что?).
"""

rod_text = """
🔵 Родительный падеж

Вопросы: Кого? Чего?

Основные значения и употребления:
Принадлежность:
Книга сестры, дом отца.
Отсутствие (с отрицанием): Нет кого? чего? —
Нет тетради, не было дождя.
Часть от целого:
Стакан чая, кусок хлеба, много народа.
После сравнительной степени:
Красивее мамы, быстрее ветра.
После некоторых глаголов и предлогов:
Бояться (кого? чего?):
Боюсь темноты.
Лишаться, достигать:
Достичь цели.

Предлоги: у, до, от, из, с, около, без, для, ради, 
вокруг, мимо: вышел из дома, жить у моря, пойти без
зонтика.
"""

dat_text = """
🟡 Дательный падеж

Вопросы: Кому? Чему?

Основные значения и употребления:
Адресат действия
Дать маме, помогать другу, советовать студенту.
Объект, для которого совершается действие:
Писать племяннице, готовить детям
Состояние или возраст субъекта
Мне холодно. Ребенку три года.
После некоторых глаголов
Верить, радоваться, угрожать, принадлежать

Предлоги: к, по, благодаря, согласно, вопреки:
идти к другу, играть по правилам, сделать благодаря вам.
"""

vin_text = """
🔴 Винительный падеж

Вопросы: Кого? Что?

Основные значения и употребления:
Прямой объект действия (на
что направлено действие): читаю книгу, 
вижу гору, люблю Родину.
Мера времени, расстояния, количества:
ждать год, пройти километр, стоить рубль.
После предлогов: в, на,
за, под, через, про,
сквозь: смотреть на
небо, положить в стол,
говорить о правду.

Важно: часто путают с именительным. 
Ключ — задать вопрос от глагола-сказуемого:
Вижу (кого? что?) слона (В.п.), но слон (И.п.) стоит.
"""

tvor_text = """
🟣 Творительный падеж

Вопросы: Кем? Чем?

Основные значения и употребления:
Орудие или средство действия:
Писать ручкой, резать ножом.
Место или путь движения:
Идти лесом, ехать полем.
Время действия:
Читать ночами, приехать весной.
Способ действия:
Говорить басом, идти шагом.
Профессия, роль, состояние (при глаголах «быть»,
«стать», «работать» и др.):
Он стал врачом. Работаю инженером.
После глаголов:
Руководить, владеть, восхищаться, гордиться.
После предлогов: с, за, под, над, между, перед: раз-
говаривать с директором, чашка под столом, небо
над городом.
"""

pred_text = """
⚫ Предложный падеж

Вопросы: О ком? О чем? В ком? В чем? На ком?
На чем? При ком? При чем? (Всегда с предлогом!)

Основные значения и употребления:
Тема мысли, речи:
Говорить о любви, думать о работе,
спорить о политике.
Местонахождение:
Находиться в библиотеке, лежать на столе,
висеть на стене.
Время действия:
Встретиться в пятницу, уехать в декабре.
Состояние, условие:
Находиться в покое, идти в дождь.
Обязательные предлоги: о/об, в/во, на, при, по. 
Без предлога не употребляется.
"""

tasks_level_1 = [
    {
        "question": "Я вижу красивый **дом**.",
        "options": ["Именительный", "Родительный", "Винительный"],
        "correct": "Винительный"
    },

{
        "question": "У меня нет старшего **брата**.",
        "options": ["Винительный", "Родительный", "Творительный"],
        "correct": "Родительный"
    },

{
        "question": "Я пишу письмо **маме**.",
        "options": ["Дательный", "Предложный", "Именительный"],
        "correct": "Дательный"
    },

{
        "question": "Я гуляю в **парке**.",
        "options": ["Предложный", "Творительный", "Родительный"],
        "correct": "Предложный"
    },

{
        "question": "Кошка играет с **клубком**.",
        "options": ["Творительный", "Родительный", "Именительный"],
        "correct": "Творительный"
    },

{
        "question": "Я восхищаюсь **смелостью**.",
        "options": ["Родительный", "Творительный", "Дательный"],
        "correct": "Творительный"
    },

{
        "question": "Поговори со **мной**.",
        "options": ["Творительный", "Предложный", "Именительный"],
        "correct": "Творительный"
    },

{
        "question": "Поздравляю тебя **с днём рождения**.",
        "options": ["Предложный", "Винительный", "Творительный"],
        "correct": "Творительный"
    },

{
        "question": "Я читаю интересную **книгу**.",
        "options": ["Именительный", "Винительный", "Родительный"],
        "correct": "Винительный"
    },

{
        "question": "Мы ждём приезда **гостей**.",
        "options": ["Родительный", "Творительный", "Дательный"],
        "correct": "Родительный"
    },
{
        "question": "Дай тетрадь **ученику**.",
        "options": ["Винительный", "Дательный", "Родительный"],
        "correct": "Дательный"
    },

{
        "question": "Дети веселятся на **празднике**.",
        "options": ["Предложный", "Творительный", "Родительный"],
        "correct": "Предложный"
    },

{
        "question": "Папа режет хлеб острым **ножом**.",
        "options": ["Именительный", "Родительный", "Творительный"],
        "correct": "Творительный"
    },

{
        "question": "Я мечтаю о **путешествии**.",
        "options": ["Винительный", "Дательный", "Предложный"],
        "correct": "Предложный"
    },

{
        "question": "Он гордится своим **сыном**.",
        "options": ["Творительный", "Именительный", "Предложный"],
        "correct": "Творительный"
    }
]

tasks_level_2 = [
    {
        "question": "Я приехал из ... (Москва)",
        "options": ["Москвы", "Москву", "Москве"],
        "correct": "Москвы"
    },

{
        "question": "Подарок для ... (моя сестра).",
        "options": ["моей сестры", "моя сестра", "моей сестре"],
        "correct": "моей сестры"
    },

{
        "question": "Книга лежит на ... (стол).",
        "options": ["стол", "стола", "столе"],
        "correct": "столе"
    },

{
        "question": "Расскажи ... (эта история).",
        "options": ["эту историю", "эта история", "этой истории"],
        "correct": "эту историю"
    },

{
        "question": "Он работает без ... (интерес).",
        "options": ["интересом", "интереса", "интересу"],
        "correct": "интереса"
    },

{
        "question": "Встречаемся у ... (вход в метро).",
        "options": ["входа в метро", "входу в метро", "вход в метро"],
        "correct": "входа в метро"
    },

{
        "question": "Цветы для ... (восьмое марта).",
        "options": ["восьмого марта", "восьмое марта", "восьмому марта"],
        "correct": "восьмого марта"
    },

{
        "question": "Мечтаю о ... (путешествие).",
        "options": ["путешествие", "путешествия", "путешествии"],
        "correct": "путешествии"
    },

{
        "question": "Письмо от … (мой друг).",
        "options": ["моего друга", "моему другу", "мой друг"],
        "correct": "моего друга"
    },

{
        "question": "Мы говорили о … (важная проблема).",
        "options": ["важная проблема", "важной проблемы", "важной проблеме"],
        "correct": "важной проблеме"
    },
{
        "question": "Вернулся из … (командировка).",
        "options": ["командировка", "командировки", "командировке"],
        "correct": "командировки"
    },

{
        "question": "Спроси у … (учитель).",
        "options": ["учителя", "учителю", "учитель"],
        "correct": "учителя"
    },

{
        "question": "Спрятался за … (большое дерево).",
        "options": ["большое дерево", "большого дерева", "большим деревом"],
        "correct": "большим деревом"
    },

{
        "question": "Сварил суп из … (свежие овощи).",
        "options": ["свежих овощей", "свежие овощи", "свежим овощам"],
        "correct": "свежих овощей"
    },

{
        "question": "Картина висит над … (диван).",
        "options": ["диваном", "дивана", "дивану"],
        "correct": "диваном"
    }
]

tasks_level_3 = [
    {
        "question": "Он никогда не расстаётся ... (свой телефон).",
        "options": ["Без своего телефона", "Со своим телефоном", "У своего телефона"],
        "correct": "Со своим телефоном"
    },

{
        "question": "Я уверен ... (свои силы) и верю в ... (удача).",
        "options": ["в своих силах и верю удаче", "в свои силы и верю в удачу", "своими силами и верю удачи"],
        "correct": "в свои силы и верю в удачу"
    },

{
        "question": "Руководитель потребовал ... (отчёт) от сотрудников.",
        "options": ["отчёта", "отчёту", "отчёт"],
        "correct": "отчёт"
    },

{
        "question": "Мама напомнила ... (сын) о ... (важная встреча).",
        "options": ["сыну о важной встрече", "сына о важной встрече", "сыном о важную встречу"],
        "correct": "сыну о важной встрече"
    },
{
        "question": "Этот фильм отличается ... (реалистичность) и интересен ... (зритель).",
        "options": ["реалистичностью и интересен зрителю", "реалистичности и интересен зрителя", "реалистичность и интересен зрителем"],
        "correct": "реалистичностью и интересен зрителю"
    },

{
        "question": "Бабушка скучает ... (внуки) и переживает за ... (они).",
        "options": ["по внукам и переживает за них", "о внуках и переживает за ними", "внуков и переживает за они"],
        "correct": "по внукам и переживает за них"
    },

{
        "question": "Он прославился ... (свои научные открытия).",
        "options": ["своими научными открытиями", "своих научных открытий", "своим научным открытиям"],
        "correct": "своими научными открытиями"
    },

{
        "question": "Заведующий отделом назначил ... (новый сотрудник) срок для выполнения задачи.",
        "options": ["новому сотруднику", "нового сотрудника", "новым сотрудником"],
        "correct": "новому сотруднику"
    },

{
        "question": "Ученик обратился за … (помощь) к … (преподаватель).",
        "options": ["помощью к преподавателю", "помощи к преподавателя", "помощь к преподавателем"],
        "correct": "помощью к преподавателю"
    },

{
        "question": "Директор поблагодарил коллектив за … (отличная работа).",
        "options": ["отличной работы", "отличную работу", "отличная работа"],
        "correct": "отличную работу"
    },

{
        "question": "Мы с интересом наблюдали за … (повадки животных).",
        "options": ["повадками животных", "повадок животных", "повадкам животных"],
        "correct": "повадками животных"
    },
{
        "question": "Я всегда советуюсь с … (родители) перед принятием решения.",
        "options": ["родителями", "родителей", "родителям"],
        "correct": "родителями"
    },

{
        "question": "Эксперт оценил проект по … (несколько критериев).",
        "options": ["нескольким критериям", "несколько критериев", "нескольких критериев"],
        "correct": "нескольким критериям"
    },

{
        "question": "От успеха этой сделки зависит … (будущее компании).",
        "options": ["будущим компании", "будущего компании", "будущее компании"],
        "correct": "будущее компании"
    }

]

tasks_level_4 = [
    {
        "question": "Согласно (приказ / приказа) директора, офис работает до 18:00.",
        "options": ["приказ", "приказа"],
        "correct": "приказа"
    },

{
        "question": "Благодаря (своевременная помощь / своевременной помощи) мы успели всё сделать",
        "options": ["своевременная помощь", "своевременной помощи"],
        "correct": "своевременной помощи"
    },

{
        "question": "По приезду / По приезде в город нужно сразу позвонить.",
        "options": ["По приезду", "По приезде"],
        "correct": "По приезде"
    },

{
        "question": "Все три (студент / студента) успешно сдали экзамен.",
        "options": ["студент", "студента"],
        "correct": "студента"
    },

{
        "question": "Он заплатил (большие деньги / больших денег) за этот старинный (альбом / альбома).",
        "options": ["большие деньги / альбом", "больших денег / альбома"],
        "correct": "большие деньги / альбом"
    },

{
        "question": "Нужно купить (килограмм апельсин / килограмм апельсинов / килограмм апельсины).",
        "options": ["килограмм апельсин", "килограмм апельсинов"],
        "correct": "килограмм апельсинов"
    },

{
        "question": "Нам не хватает (ещё один человек / ещё одного человека) для команды.",
        "options": ["ещё один человек", "ещё одного человека"],
        "correct": "ещё одного человека"
    },
{
        "question": "Докладчик остановился (на вопросе / на вопрос) об экологии.",
        "options": ["на вопросе", "на вопрос"],
        "correct": "на вопросе"
    },

{
        "question": "Вопреки (все прогнозы / всем прогнозам) погода была прекрасной.",
        "options": ["все прогнозы", "всем прогнозам"],
        "correct": "всем прогнозам"
    },

{
        "question": "В течение (последняя неделя / последней недели) мы ждали ответа.",
        "options": ["последняя неделя", "последней недели"],
        "correct": "последней недели"
    },

{
        "question": "У него не было (никакие сомнения / никаких сомнений) в (правильность / правильности) решения.",
        "options": ["никакие сомнения / правильность", "никаких сомнений / правильности"],
        "correct": "никаких сомнений / правильности"
    },

{
        "question": "Девушка с (светлые волосы / светлыми волосами) и (голубые глаза / голубыми глазами) стояла у входа",
        "options": ["светлые волосы / голубые глаза", "светлыми волосами / голубыми глазами"],
        "correct": "светлыми волосами / голубыми глазами"
    },

{
        "question": "Мы ищем менеджера, разбирающегося в (работа / работе) с базами данных.",
        "options": ["работа", "работе"],
        "correct": "работе"
    },

{
        "question": "К (окончание / окончанию) переговоров стороны пришли к согласию.",
        "options": ["окончание", "окончанию"],
        "correct": "окончанию"
    },

{
        "question": "Прошу предоставить мне (отпуск / отпуска) с 1 по 10 июня.",
        "options": ["отпуск", "отпуска"],
        "correct": "отпуск"
    }
]

tasks_by_level = {
    "🟢 Уровень 1": tasks_level_1,
    "🟡 Уровень 2": tasks_level_2,
    "🔵 Уровень 3": tasks_level_3,
    "🔴 Уровень 4": tasks_level_4
}

level_descriptions = {
    "🟢 Уровень 1": "Определи падеж выделенного слова.",
    "🟡 Уровень 2": "Вставь подходящее по смыслу слово в правильном падеже.",
    "🔵 Уровень 3": "Закончи предложение, выбрав правильную форму и, если нужно, предлог.",
    "🔴 Уровень 4": "Выбери правильный ответ."
}

current_level = {}
current_task = {}

# --- ХЕНДЛЕРЫ ---
@dp.message(lambda message: message.text == "/start")
async def start(message: types.Message):
    await message.answer("Привет! 👋 Выбери раздел:", reply_markup=main_kb)

@dp.message(lambda message: message.text == "📘 Теория")
async def theory(message: types.Message):
    await message.answer("Выбери тему:", reply_markup=theory_kb)

@dp.message(lambda message: message.text == "📝 Задания")
async def tasks(message: types.Message):
    await message.answer("Выбери уровень:", reply_markup=levels_kb)

@dp.message(lambda message: message.text in tasks_by_level)
async def select_level(message: types.Message):
    user_id = message.from_user.id
    level = message.text 
    current_level[user_id] = level

    description = level_descriptions.get(level, "")

    await message.answer(
        f"{level}\n\n📌 {description}",
    )

    await message.answer("Выбери задание:", reply_markup=get_tasks_keyboard(level))

@dp.message(lambda message: message.text == "📌 Все падежи")
async def all_cases(message: types.Message):
    await message.answer(theory_text)

@dp.message(lambda message: message.text == "🟢 Именительный")
async def imen(message: types.Message):
    await message.answer(imen_text)

@dp.message(lambda message: message.text == "🔵 Родительный")
async def rod(message: types.Message):
    await message.answer(rod_text)

@dp.message(lambda message: message.text == "🟡 Дательный")
async def dat(message: types.Message):
    await message.answer(dat_text)

@dp.message(lambda message: message.text == "🔴 Винительный")
async def vin(message: types.Message):
    await message.answer(vin_text)

@dp.message(lambda message: message.text == "🟣 Творительный")
async def tvor(message: types.Message):
    await message.answer(tvor_text)

@dp.message(lambda message: message.text == "⚫ Предложный")
async def pred(message: types.Message):
    await message.answer(pred_text)


@dp.message(lambda message: message.text.startswith("Задание"))
async def show_task(message: types.Message):
    user_id = message.from_user.id
    level = current_level.get(user_id)
    if not level:
        await message.answer("Выбери уровень сначала", reply_markup=levels_kb)
        return

    index = int(message.text.split()[1]) - 1
    task = tasks_by_level[level][index]
    current_task[user_id] = index
    
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=opt)] for opt in task["options"]] + 
                 [[KeyboardButton(text="➡️ Следующее"), KeyboardButton(text="⬅️ Назад")]],
        resize_keyboard=True
    )
    
    await message.answer(task["question"], reply_markup=kb, parse_mode="HTML")

@dp.message(lambda message: message.text == "➡️ Следующее")
async def next_task(message: types.Message):
    user_id = message.from_user.id
    if user_id not in current_task or user_id not in current_level:
        return
    
    level = current_level[user_id]
    index = current_task[user_id] + 1
    tasks = tasks_by_level[level]
    
    if index >= len(tasks):
        await message.answer("🎉 Задания закончились!", reply_markup=get_tasks_keyboard(level))
        del current_task[user_id]
        return
    
    current_task[user_id] = index
    task = tasks[index]
    
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=opt)] for opt in task["options"]] + 
                 [[KeyboardButton(text="➡️ Следующее"), KeyboardButton(text="⬅️ Назад")]],
        resize_keyboard=True
    )
    
    await message.answer(task["question"], reply_markup=kb)

@dp.message(lambda message: message.text == "⬅️ Назад")
async def back(message: types.Message):
    user_id = message.from_user.id
    
    if user_id in current_task:
        # Пользователь был в задании → возвращаем к списку заданий того уровня
        level = current_level.get(user_id)
        if level:
            await message.answer("Выбери задание:", reply_markup=get_tasks_keyboard(level))
        else:
            # На всякий случай, если уровень потерян
            await message.answer("Выбери уровень:", reply_markup=levels_kb)
        del current_task[user_id]  # очищаем текущую задачу
    elif user_id in current_level:
        # Пользователь был на экране выбора задания → возвращаем к выбору уровня
        await message.answer("Выбери уровень:", reply_markup=levels_kb)
        del current_level[user_id]
    else:
        # Пользователь был в главном меню/теории → возвращаем к главному меню
        await message.answer("Главное меню:", reply_markup=main_kb)

@dp.message(lambda message: message.from_user.id in current_task)
async def check_answer(message: types.Message):
    user_id = message.from_user.id
    level = current_level.get(user_id)
    if not level:
        return
    
    index = current_task[user_id]
    task = tasks_by_level[level][index]
    
    if message.text == task["correct"]:
        await message.answer("✅ Правильно!")
    elif message.text in task["options"]:
        await message.answer("❌ Неправильно")

def get_tasks_keyboard(level):
    tasks = tasks_by_level[level]
    buttons = [[KeyboardButton(text=f"Задание {i+1}")] for i in range(len(tasks))]
    buttons.append([KeyboardButton(text="⬅️ Назад")])
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- ЗАПУСК ---
async def main():
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Web server running on port {port}")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
