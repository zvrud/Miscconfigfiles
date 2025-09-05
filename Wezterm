-- Pull in the wezterm API
local wezterm = require 'wezterm'
local act = wezterm.action

-- This will hold the configuration.
local config = wezterm.config_builder()

-- color scheme toggling
--wezterm.on("toggle-colorscheme", function(window, pane)
--  local overrides = window:get_config_overrides() or {}
--  if overrides.color_scheme == "Zenburn" then
--    overrides.color_scheme = "Cloud (terminal.sexy)"
--  else
--    overrides.color_scheme = "Zenburn"
--  end
--  window:set_config_overrides(overrides)
--end)

config = {
  --front_end = "OpenGL",                            
  --front_end = "Software",                            
  front_end = "WebGpu",                            
  --default_prog = { "powershell.exe", "-NoLogo" },
  default_prog = { "powershell.exe" },
  --default_prog = { 'wsl.exe' },
  --initial_cols = 80,
  --max_fps = 144,
  --animation_fps = 1,         
  --cursor_blink_rate = 500,
  --term = "xterm-256color", -- Set the terminal type
  --cell_width = 0.9,
  window_background_opacity = 0.9,
  --text_background_opacity = 0.85,
  --prefer_egl = true,


  -- tab 
  --enable_tab_bar = false,
  hide_tab_bar_if_only_one_tab = true,
  use_fancy_tab_bar = false,
  --tab_bar_at_bottom = true,
  
  -- window
  --window_decorations = "NONE | RESIZE"
  window_decorations = "RESIZE", -- disable the title bar but enable the resizable border
  window_padding = {
    left = 0,
    right = 0,
    top = 0,
    bottom = 0,
  },
  
  window_close_confirmation = "NeverPrompt", -- exit
  
  keys = {

    -- tmux

    -- pane
    { key = "t", mods = "ALT",    action = wezterm.action.SpawnTab "DefaultDomain" },
    { key = "m", mods = "ALT",    action = wezterm.action.ShowTabNavigator },
    { key = "w", mods = "ALT",    action = wezterm.action.CloseCurrentPane { confirm = true } },

    -- split
    { key = "v", mods = "ALT",    action = wezterm.action.SplitHorizontal { domain = "CurrentPaneDomain" } },
    { key = "h", mods = "ALT",    action = wezterm.action.SplitVertical { domain = "CurrentPaneDomain" } },
   
    -- activate
    { key = "y", mods = "ALT",    action = wezterm.action.ActivatePaneDirection "Left" },
    { key = "n", mods = "ALT",    action = wezterm.action.ActivatePaneDirection "Down" },
    { key = "e", mods = "ALT",    action = wezterm.action.ActivatePaneDirection "Up" },
    { key = "o", mods = "ALT",    action = wezterm.action.ActivatePaneDirection "Right" },

   -- resize pane
    { key = "Y", mods = "ALT",    action = wezterm.action.AdjustPaneSize { "Left", 5 } },
    { key = "N", mods = "ALT",    action = wezterm.action.AdjustPaneSize { "Down", 5 } },
    { key = "E", mods = "ALT",    action = wezterm.action.AdjustPaneSize { "Up", 5 } },
    { key = "O", mods = "ALT",    action = wezterm.action.AdjustPaneSize { "Right", 5 } },

  -- activate tab
    { key = "1", mods = "ALT",    action = wezterm.action.ActivateTab(0) },
    { key = "2", mods = "ALT",    action = wezterm.action.ActivateTab(1) },
    { key = "3", mods = "ALT",    action = wezterm.action.ActivateTab(2) },
    { key = "4", mods = "ALT",    action = wezterm.action.ActivateTab(3) },
    { key = "5", mods = "ALT",    action = wezterm.action.ActivateTab(4) },
    { key = "6", mods = "ALT",    action = wezterm.action.ActivateTab(5) },
    { key = "7", mods = "ALT",    action = wezterm.action.ActivateTab(6) },
    { key = "8", mods = "ALT",    action = wezterm.action.ActivateTab(7) },
    { key = "9", mods = "ALT",    action = wezterm.action.ActivateTab(-1) },

    { key = "9", mods = "CTRL", action = act.PaneSelect },
    { key = "L", mods = "CTRL", action = act.ShowDebugOverlay },
    {
      key = "O",
      mods = "CTRL|ALT",
      -- toggling opacity
      action = wezterm.action_callback(function(window, _)
        local overrides = window:get_config_overrides() or {}
        if overrides.window_background_opacity == 1.0 then
          overrides.window_background_opacity = 0.85
        else
          overrides.window_background_opacity = 1.0
        end
        window:set_config_overrides(overrides)
      end),
    },
  },


  -- font
  --font = wezterm.font("Iosevka Custom"),
  --font = wezterm.font("Agave Nerd Font Mono"),
  font = wezterm.font("CaskaydiaCove Nerd Font Mono"),
  font_size = 12.0,
 
  -- color
  default_cursor_style = "BlinkingBlock",
  --color_scheme = "Nord (Gogh)",
  color_scheme = "Cloud (terminal.sexy)",

  colors = {
    -- background = '#3b224c',
    -- background = "#181616", -- vague.nvim bg
    -- background = "#080808", -- almost black
    --background = "#0c0b0f", -- dark purple
    
    --background = "#302c3b", -- dark purple
    background = "#3c374a", -- dark purple
    
    -- background = "#020202", -- dark purple
    -- background = "#17151c", -- brighter purple
    -- background = "#16141a",
    -- background = "#0e0e12", -- bright washed lavendar
    -- background = 'rgba(59, 34, 76, 100%)',
    cursor_border = "#bea3c7",
    -- cursor_fg = "#281733",
    cursor_bg = "#bea3c7",
    -- selection_fg = '#281733',

    tab_bar = {
      background = "#0c0b0f",
      -- background = "rgba(0, 0, 0, 0%)",
      active_tab = {
        bg_color = "#0c0b0f",
        fg_color = "#bea3c7",
        intensity = "Normal",
        underline = "None",
        italic = false,
        strikethrough = false,
      },
      inactive_tab = {
        bg_color = "#0c0b0f",
        fg_color = "#f8f2f5",
        intensity = "Normal",
        underline = "None",
        italic = false,
        strikethrough = false,
      },

      new_tab = {
        -- bg_color = "rgba(59, 34, 76, 50%)",
        bg_color = "#0c0b0f",
        fg_color = "white",
      },
    },
  },
  

  --window_frame = {
    --font = wezterm.font({ family = "Iosevka Custom", weight = "Regular" }),
    --active_titlebar_bg = "#0c0b0f",
    -- active_titlebar_bg = "#181616",
  --},


}



-- Finally, return the configuration to wezterm:
return config
