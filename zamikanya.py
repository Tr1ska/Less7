def helper(work):
    insert_in_memory = work

    def helper(work):
        return f"Я можу допомогти із {insert_in_memory}, а після цього хочу допомогти із {work}"
    return helper

helper = helper("homework")
print(helper("cleaning"))
print(helper("driving"))