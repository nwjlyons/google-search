import webbrowser
import sublime, sublime_plugin

class GoogleSearchCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        querys = []
        for region in self.view.sel():
            if region.empty():
                # if we have no selection grab the current word
                word = self.view.word(region)
                if not word.empty():
                    querys.append(self.view.substr(word))
            else:
                # append the selection
                if not region.empty():
                    querys.append(self.view.substr(region))


        if len(querys) != 0:
            selection = " ".join(querys)
            webbrowser.open("http://www.google.com/search?q=%s" % selection)
        else:
            print("Google Search Plugin: Nothing to search !")

