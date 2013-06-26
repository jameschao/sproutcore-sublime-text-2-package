import sublime, sublime_plugin

class SproutCoreListener(sublime_plugin.EventListener):
  def on_post_save(self, view):
    view.window().run_command('build')
