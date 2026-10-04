import flet as ft
import random

# База вопросов для 6 класса: 10 лёгких, 10 средних, 10 сложных
TEMPLATES = [
    # ------------------ ЛЁГКИЕ (10 вопросов) ------------------
    {
        "sentence": "Собака неожиданно выскочила _____ куста.",
        "options": ["из-за", "из за", "из-под", "с-за"],
        "correct": "из-за",
        "level": "🟢 Легкий",
        "explanation": "Сложносоставной предлог «из-за» пишется через дефис."
    },
    {
        "sentence": "Птица вылетела _____ густых ветвей дерева.",
        "options": ["из-под", "из под", "из-за", "с-под"],
        "correct": "из-под",
        "level": "🟢 Легкий",
        "explanation": "Предлог «из-под» всегда пишется через дефис."
    },
    {
        "sentence": "Мы перебрались _____ узкий ручей по мостику.",
        "options": ["через", "через-за", "сквозь", "вдоль"],
        "correct": "через",
        "level": "🟢 Легкий",
        "explanation": "Простой предлог «через» указывает на пересечение пространства."
    },
    {
        "sentence": "Ласточки кружили _____ нашей крышей.",
        "options": ["над", "надо", "под", "около"],
        "correct": "над",
        "level": "🟢 Легкий",
        "explanation": "Простой предлог «над» с творительным падежом."
    },
    {
        "sentence": "Кот пробрался в дом _____ открытую форточку.",
        "options": ["через", "сквозь", "из-за", "вдоль"],
        "correct": "через",
        "level": "🟢 Легкий",
        "explanation": "Пространственное значение предлога «через»."
    },
    {
        "sentence": "Тучи медленно двигались _____ горизонтом.",
        "options": ["над", "под", "из-за", "около"],
        "correct": "над",
        "level": "🟢 Легкий",
        "explanation": "Простой пространственный предлог «над»."
    },
    {
        "sentence": "Дети стояли _____ старого дуба и слушали птиц.",
        "options": ["около", "о коло", "вдоль", "возле по"],
        "correct": "около",
        "level": "🟢 Легкий",
        "explanation": "Предлог «около» указывает на нахождение вблизи объекта."
    },
    {
        "sentence": "Мы прошли _____ густой туман к опушке леса.",
        "options": ["сквозь", "через-за", "из-за", "над"],
        "correct": "сквозь",
        "level": "🟢 Легкий",
        "explanation": "Предлог «сквозь» указывает на движение внутри среды."
    },
    {
        "sentence": "Ученик справился с задачей _____ всяких затруднений.",
        "options": ["без", "безо", "из-за", "под"],
        "correct": "без",
        "level": "🟢 Легкий",
        "explanation": "Простой предлог «без» указывает на отсутствие чего-либо."
    },
    {
        "sentence": "Малыш спрятался _____ большой деревянный стол.",
        "options": ["под", "подо", "над", "из-под"],
        "correct": "под",
        "level": "🟢 Легкий",
        "explanation": "Простой предлог «под» указывает на нахождение ниже объекта."
    },

    # ------------------ СРЕДНИЕ (10 вопросов) ------------------
    {
        "sentence": "Мы не спеша шли _____ берега реки.",
        "options": ["вдоль", "в доли", "вдоли", "вдоль по"],
        "correct": "вдоль",
        "level": "🟡 Средний",
        "explanation": "Наречный предлог «вдоль» пишется слитно."
    },
    {
        "sentence": "Ребята выбежали _____ приехавшим гостям.",
        "options": ["навстречу", "на встречу", "вслед", "наперекор"],
        "correct": "навстречу",
        "level": "🟡 Средний",
        "explanation": "Предлог «навстречу» (направление) пишется слитно."
    },
    {
        "sentence": "_____ обеда мы решили немного прогуляться.",
        "options": ["Вместо", "В место", "В замен", "Вместе"],
        "correct": "Вместо",
        "level": "🟡 Средний",
        "explanation": "Предлог «вместо» со значением замещения пишется слитно."
    },
    {
        "sentence": "Матч состоялся _____ проливной дождь.",
        "options": ["несмотря на", "не смотря на", "невзирая на", "вследствие"],
        "correct": "несмотря на",
        "level": "🟡 Средний",
        "explanation": "Предлог «несмотря на» пишется слитно с «не»."
    },
    {
        "sentence": "Занятия отложили _____ болезни учителя.",
        "options": ["по причине", "попричине", "из за", "ввиду"],
        "correct": "по причине",
        "level": "🟡 Средний",
        "explanation": "Предложное сочетание «по причине» всегда пишется раздельно."
    },
    {
        "sentence": "Лодка двигалась _____ сильного течения.",
        "options": ["наперекор", "на перекор", "вопреки", "вдоль"],
        "correct": "наперекор",
        "level": "🟡 Средний",
        "explanation": "Предлог «наперекор» пишется слитно."
    },
    {
        "sentence": "Мы шли _____ следам ушедшего отряда.",
        "options": ["вслед за", "в след за", "вследза", "вслед"],
        "correct": "вслед за",
        "level": "🟡 Средний",
        "explanation": "Составной предлог «вслед за» пишется раздельно."
    },
    {
        "sentence": "Дежурный сделал всё _____ инструкциям.",
        "options": ["согласно", "согласно с", "в соответствие", "по"],
        "correct": "согласно",
        "level": "🟡 Средний",
        "explanation": "Предлог «согласно» употребляется с дательным падежом (чему?)."
    },
    {
        "sentence": "Сспортсмен действовал _____ правилам соревнований.",
        "options": ["вопреки", "во преки", "наперекор", "согласно"],
        "correct": "вопреки",
        "level": "🟡 Средний",
        "explanation": "Предлог «вопреки» пишется слитно."
    },
    {
        "sentence": "Мы шли в темноте _____ мерцающего огонька.",
        "options": ["наподобие", "навстречу", "направление", "в сторону"],
        "correct": "навстречу",
        "level": "🟡 Средний",
        "explanation": "Предлог «навстречу» указывает направление движения."
    },

    # ------------------ СЛОЖНЫЕ (10 вопросов) ------------------
    {
        "sentence": "Поезд задерживался _____ получаса.",
        "options": ["в течение", "в течении", "в продолжение", "в следствие"],
        "correct": "в течение",
        "level": "🔴 Сложный",
        "explanation": "Предлог «в течение» (время) пишется раздельно и с «е» на конце."
    },
    {
        "sentence": "_____ нескольких дней шёл сильный снегопад.",
        "options": ["В продолжение", "В продолжении", "В течение", "Втечение"],
        "correct": "В продолжение",
        "level": "🔴 Сложный",
        "explanation": "«В продолжение» (длительность) пишется раздельно с «е»."
    },
    {
        "sentence": "Экскурсию отменили _____ неблагоприятных условий.",
        "options": ["вследствие", "в следствие", "в следствии", "из-за"],
        "correct": "вследствие",
        "level": "🔴 Сложный",
        "explanation": "Предлог «вследствие» = «из-за», пишется слитно с «е»."
    },
    {
        "sentence": "_____ надвигающегося шторма корабли зашли в порт.",
        "options": ["Ввиду", "В виду", "Вследствие", "По причине"],
        "correct": "Ввиду",
        "level": "🔴 Сложный",
        "explanation": "Предлог «ввиду» (причина) пишется слитно."
    },
    {
        "sentence": "Облако на горизонте было _____ огромного дракона.",
        "options": ["наподобие", "на подобие", "в виде", "подобно"],
        "correct": "наподобие",
        "level": "🔴 Сложный",
        "explanation": "Предлог «наподобие» пишется слитно."
    },
    {
        "sentence": "Вам необходимо иметь это _____ при принятии решения.",
        "options": ["в виду", "ввиду", "в виде", "в течение"],
        "correct": "в виду",
        "level": "🔴 Сложный",
        "explanation": "Фразеологизм «иметь в виду» пишется раздельно!"
    },
    {
        "sentence": "Существенные факты выяснились _____ по делу.",
        "options": ["в следствии", "вследствие", "в следствие", "в течение"],
        "correct": "в следствии",
        "level": "🔴 Сложный",
        "explanation": "«В следствии» — существительное с предлогом (где? в чём?)."
    },
    {
        "sentence": "Герои плыли дальше, всматриваясь _____ реки.",
        "options": ["в течение", "в течении", "в продолжение", "в следствие"],
        "correct": "в течение",
        "level": "🔴 Сложный",
        "explanation": "«В течение» реки — существительное с предлогом (в чём?)."
    },
    {
        "sentence": "_____ плохого самочувствия ему пришлось остаться дома.",
        "options": ["Ввиду", "В виду", "В следствие", "В течение"],
        "correct": "Ввиду",
        "level": "🔴 Сложный",
        "explanation": "Предлог «ввиду» указывает на причину и пишется слитно."
    },
    {
        "sentence": "Ученик долго всматривался _____ быстрого ручья.",
        "options": ["в течение", "в течении", "в продолжении", "в следствие"],
        "correct": "в течение",
        "level": "🔴 Сложный",
        "explanation": "Предлог «в течение» оканчивается на «е»."
    }
]


def main(page: ft.Page):
    page.title = "Тренажёр предлогов"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 12
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    # Настройки для эмуляции мобильного экрана в браузере / десктопе
    page.window.width = 390
    page.window.height = 780

    score = 0
    streak = 0
    max_streak = 0
    total_answered = 0

    deck = []

    def get_next_question():
        nonlocal deck
        if not deck:
            deck = TEMPLATES.copy()
            random.shuffle(deck)
        return deck.pop()

    current_q = None

    # Заголовок и карточки
    title_text = ft.Text("Предлоги", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)

    level_badge = ft.Text("", size=12, weight=ft.FontWeight.W_500, color=ft.Colors.GREY_700)
    score_label = ft.Text("Очки: 0", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
    streak_label = ft.Text("🔥 0", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700)
    record_label = ft.Text("🏆 0", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.AMBER_800)

    card_sentence = ft.Text("", size=17, weight=ft.FontWeight.W_600, text_align=ft.TextAlign.CENTER)
    explanation_text = ft.Text("", size=13, color=ft.Colors.BLUE_GREY_800, italic=True, text_align=ft.TextAlign.CENTER)

    options_container = ft.Column(spacing=10, horizontal_alignment=ft.CrossAxisAlignment.STRETCH)

    def load_question():
        nonlocal current_q
        current_q = get_next_question()

        level_badge.value = f"Сложность: {current_q['level']}"
        card_sentence.value = current_q["sentence"]
        explanation_text.value = ""

        options_container.controls.clear()

        opts = current_q["options"].copy()
        random.shuffle(opts)

        for option in opts:
            btn = ft.Button(
                content=ft.Text(option, size=16, weight=ft.FontWeight.W_500),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=14),
                    padding=16,
                ),
                on_click=lambda e, opt=option: check_answer(opt)
            )
            btn.data = option
            options_container.controls.append(btn)

        page.update()

    def check_answer(selected_option):
        nonlocal score, streak, max_streak, total_answered
        total_answered += 1

        for btn in options_container.controls:
            if isinstance(btn, ft.Button):
                btn.disabled = True
                option_text = btn.data

                if option_text == current_q["correct"]:
                    btn.style.bgcolor = ft.Colors.GREEN_200
                    btn.style.color = ft.Colors.GREEN_900
                elif option_text == selected_option and selected_option != current_q["correct"]:
                    btn.style.bgcolor = ft.Colors.RED_200
                    btn.style.color = ft.Colors.RED_900

        if selected_option == current_q["correct"]:
            streak += 1
            score += 10 + (streak * 2)
            if streak > max_streak:
                max_streak = streak
            explanation_text.value = f"✅ Верно!\n{current_q['explanation']}"
        else:
            streak = 0
            explanation_text.value = f"❌ Ошибка!\n{current_q['explanation']}"

        score_label.value = f"Очки: {score}"
        streak_label.value = f"🔥 {streak}"
        record_label.value = f"🏆 {max_streak}"

        next_btn = ft.Button(
            content=ft.Text("Следующий вопрос ➔", size=16, weight=ft.FontWeight.BOLD),
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.BLUE_600,
                color=ft.Colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=14),
                padding=14
            ),
            on_click=lambda e: load_question()
        )
        options_container.controls.append(
            ft.Container(content=next_btn, margin=ft.Margin(0, 12, 0, 0))
        )

        page.update()

    # Шапка приложения (Мобильный Header)
    header = ft.Card(
        content=ft.Container(
            content=ft.Row(
                [score_label, streak_label, record_label],
                alignment=ft.MainAxisAlignment.SPACE_AROUND
            ),
            padding=12
        ),
        elevation=2
    )

    # Карточка с заданием
    question_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    level_badge,
                    card_sentence,
                    explanation_text,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12
            ),
            padding=20
        ),
        elevation=3
    )

    page.add(
        ft.Column(
            [
                title_text,
                header,
                question_card,
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                options_container
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            width=360
        )
    )

    load_question()


if __name__ == "__main__":
    ft.run(main)