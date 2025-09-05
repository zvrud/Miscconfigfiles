
config.load_autoconfig(False)
c.content.blocking.enabled = True

# privacy
# c.content.canvas_reading = False
# c.content.geolocation = False
# c.content.webrtc_ip_handling_policy = "default-public-interface-only"
# c.completion.open_categories = ['filesystem']


c.window.hide_decoration = True
c.tabs.show = "never"
# c.content.fullscreen.window = True # Limit fullscreen to browser window
c.scrolling.bar = "always"

# c.zoom.default = 100
# c.zoom.levels = ["25%", "33%", "50%", "67%", "75%", "90%", "100%", "125%", "133%", "150%", "175%", "200%", "250%", "300%"]
# c.fonts.web.size.default = 20 # webpage
c.fonts.default_size = '10pt'

# c.colors.webpage.darkmode.enabled = True
# c.colors.webpage.darkmode.policy.images = 'never'
# c.colors.webpage.bg = '#191919' # fix darkmode white flash



# c.url.start_pages = 'file:///dev/null'
# c.url.default_page= 'file:///dev/null'
c.url.start_pages = "https://google.com/"
# c.url.default_page= 'https://google.com/search?q={}'

c.url.searchengines = {
    'DEFAULT': 'https://google.com/search?q={}',
    'gi': 'https://github.com/search?q={}',
    'wd': 'https://en.wikipedia.org/wiki/Special:Search?search={}',
    'you': 'https://youdao.com/result?word={}&lang=en'
}



# c.downloads.location.directory = "~/dls"
c.downloads.location.directory = "~/Downloads"
c.downloads.position = "bottom"



# c.colors.statusbar.normal.bg = '#427b58'
# c.colors.statusbar.command.bg = '#427b58'
# c.colors.statusbar.insert.bg = '#b16286'
# c.colors.statusbar.normal.fg = '#eeeeee'
# c.colors.statusbar.command.fg = '#eeeeee'
# c.colors.hints.bg = '#427b58'
# c.colors.hints.match.fg = '#eeeeee'




c.editor.command = ['foot', '-T', 'Floating_Term', 'nvim', '{file}', '-c', 'normal {line}G{column0}l']







#c.content.proxy = "http://localhost:PORT"













# key bindings 

##normal
# y - h
# o -l 
# n - u
# u - j

config.bind('y', 'scroll left')
config.bind('n', 'scroll down')
config.bind('e', 'scroll up')
config.bind('o', 'scroll right')

config.bind('h', 'hint links yank')
config.bind('H', 'hint links yank-primary')
config.bind('l', 'cmd-set-text -s :open')
config.bind('L', 'cmd-set-text -s :open -t')
config.bind('u', 'search-next')
config.bind('U', 'search-prev')
config.bind('j', 'undo')
config.bind('J', 'undo-w')


# config.bind('<Ctrl-Shift-m>', 'spawn mpv {url}')
# config.bind('M', 'hint links spawn mpv {hint-url}')
config.bind('A', 'hint links spawn mpv {hint-url}')



## caret

config.bind('y', 'move-to-prev-char', mode='caret')
config.bind('n', 'move-to-next-line', mode='caret')
config.bind('e', 'move-to-prev-line', mode='caret')
config.bind('o', 'move-to-next-char', mode='caret')


## others



config.bind('cs', 'config-source')

config.bind('zi', 'zoom-in')
config.bind('zo', 'zoom-out')

config.bind('si', 'hint images download')

config.bind('<Ctrl-p>', 'completion-item-focus --history prev', mode='command')
config.bind('<Ctrl-n>', 'completion-item-focus --history next', mode='command')

config.bind('gp', 'open -p')


aliases = {
    "source": "config-source",
}


