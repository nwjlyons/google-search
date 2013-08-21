import webbrowser
import sublime, sublime_plugin

class GoogleSearchCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        selection = ""
        for region in self.view.sel():
            # Concatenate selected regions together.
            selection += self.view.substr(region)

        webbrowser.open("http://www.google.com/search?q=%s" % selection)

    def is_visible(self):

        is_visible = False

        # Only enable menu option if at least one region contains selected text.
        for region in self.view.sel():
            if not region.empty():
                is_visible = True

        return is_visible

    def is_enabled(self):
        return self.is_visible()