from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class IButton(ABC):
  @abstractmethod
  def render(self): pass


class IDropDown(ABC):
  @abstractmethod
  def render(self): pass


class ITextBox(ABC):
  @abstractmethod
  def render(self): pass


class IThemeFactory(ABC):
  @abstractmethod
  def create_button(self) -> IButton: pass

  @abstractmethod
  def create_drop_down(self) -> IDropDown: pass

  @abstractmethod
  def create_text_box(self) -> ITextBox: pass


#Linux Concret classes and Factory
class LinuxButton(IButton):
  def render(self):
    print("🐧 Rendering Linux Button 🐧")

class LinuxDropDown(IDropDown):
  def render(self):
    print("🐧 Rendering Linux Dropdown")

class LinuxTextBox(ITextBox):
  def render(self):
    print("🐧 Rendering Linux TextBox")


class LinuxFactory(IThemeFactory):
  def create_button(self):
    return LinuxButton()

  def create_drop_down(self):
    return LinuxDropDown()

  def create_text_box(self):
    return LinuxTextBox()


# MAC
class MacButton(IButton):
  def render(self):
    print("🍎 Rendering Mac button")

class MacDropDown(IDropDown):
  def render(self):
    print("🍎 Rendering MAC Dropdown")

class MacTextBox(ITextBox):
  def render(self):
    print("🍎 Rendering MAC Text Box")


class MacFactory(IThemeFactory):
  def create_button(self):
    return MacButton()

  def create_drop_down(self):
    return MacDropDown()

  def create_text_box(self):
    return MacTextBox()


# Window
class WinButton(IButton):
  def render(self):
    print("🪟 Rendering window button")

class WinDropDown(IDropDown):
  def render(self):
    print("🪟 Rendering window dropdown")

class WinTextBox(ITextBox):
  def render(self):
    print("🪟 Rendering window textbox")


class WindowFactory(IThemeFactory):
  def create_button(self):
    return WinButton()

  def create_drop_down(self):
    return WinDropDown()

  def create_text_box(self):
    return WinTextBox()
  
linux_factory = LinuxFactory()
linux_button = linux_factory.create_button()
linux_button.render()

win_factory = WindowFactory()
win_drop_down = win_factory.create_drop_down()
win_drop_down.render()