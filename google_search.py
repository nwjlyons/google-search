import webbrowser
import sublime, sublime_plugin

class GoogleSearchCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        selection = ""
        for region in self.view.sel():
            word = self.view.word(region)
            if not word.empty():
                selection += " " + self.view.substr(word)

        webbrowser.open("http://www.google.com/search?q=%s" % selection)

