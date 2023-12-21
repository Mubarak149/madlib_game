class Madlib:
    def __init__(self):
        self._var_names = []

    def story_modified(self,story,deli=" ",*vars):
        for variable in story.split(deli):
            if variable in vars and variable not in self._var_names:
                self._var_names.append(variable)


        for variable in self._var_names:
            user_word = input(f"Put a {variable}: ")
            story = story.replace(variable, user_word)

        return story



madlib = Madlib()

# story = "my Name is name i am in class_Name i want to be a career_choice"
# print(madlib.story_modified(story," " ,"name","class_Name","career_choice"))
# madlib.story_modified(pass your story(story), what separate each word in your story(deli),
# pass the words you want to change(*vars))

#it appear in the next version
