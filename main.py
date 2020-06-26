from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from re import search
from markdown import markdown
from pyperclip import copy


class MainUi(object):
    def __init__(self):
        self.centralwidget = QtWidgets.QWidget(frame)
        self.vertical_layout_widget = QtWidgets.QWidget(self.centralwidget)
        self.vertical_layout_widget.setGeometry(QtCore.QRect(0, 0, 820, 400))
        self.vertical_layout = QtWidgets.QVBoxLayout(self.vertical_layout_widget)
        self.horizontal_layout_text = QtWidgets.QHBoxLayout()
        self.horizontal_layout_styles = QtWidgets.QHBoxLayout()
        self.horizontal_layout_colors = QtWidgets.QHBoxLayout()
        self.horizontal_layout_shields = QtWidgets.QHBoxLayout()
        self.horizontal_layout_buttons = QtWidgets.QHBoxLayout()

    def setup_ui(self, frame):
        frame.resize(820, 400)
        frame.setAutoFillBackground(True)
        frame.setWindowTitle("Easy badges for Readme.MD on GitHub Repo")

        # Fonts
        bold_font = QtGui.QFont()
        bold_font.setPointSize(12)
        bold_font.setBold(True)

        simple_font = QtGui.QFont()
        simple_font.setPointSize(10)

        # Elements
        ## Repository data
        self.label_repository = QtWidgets.QLabel(self.vertical_layout_widget)
        self.label_repository.setFont(bold_font)
        self.label_repository.setAlignment(QtCore.Qt.AlignCenter)
        self.label_repository.setText("Repository data")
        self.vertical_layout.addWidget(self.label_repository)

        self.label_profile = QtWidgets.QLabel(self.vertical_layout_widget)
        self.label_profile.setFont(simple_font)
        self.label_profile.setText("Profile:")
        self.horizontal_layout_text.addWidget(self.label_profile)

        self.tf_github_profile = QtWidgets.QLineEdit(self.vertical_layout_widget)
        self.tf_github_profile.setFont(simple_font)
        self.tf_github_profile.setToolTip("GitHub Profile Name")
        self.horizontal_layout_text.addWidget(self.tf_github_profile)

        self.label_repo = QtWidgets.QLabel(self.vertical_layout_widget)
        self.label_repo.setFont(simple_font)
        self.label_repo.setText("Repo:")
        self.horizontal_layout_text.addWidget(self.label_repo)

        self.tf_github_repo = QtWidgets.QLineEdit(self.vertical_layout_widget)
        self.tf_github_repo.setFont(simple_font)
        self.tf_github_repo.setToolTip("GitHub Repository Name")
        self.horizontal_layout_text.addWidget(self.tf_github_repo)
        self.horizontal_layout_text.setStretch(3, 2)
        self.vertical_layout.addLayout(self.horizontal_layout_text)

        ## Styles
        self.rb_group_styles = QtWidgets.QButtonGroup(frame)

        self.label_styles = QtWidgets.QLabel(self.vertical_layout_widget)
        self.label_styles.setFont(bold_font)
        self.label_styles.setAlignment(QtCore.Qt.AlignCenter)
        self.label_styles.setText("Styles")
        self.vertical_layout.addWidget(self.label_styles)

        self.rb_style_plastic = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_style_plastic.setFont(simple_font)
        self.rb_style_plastic.setText("Plastic")
        self.rb_group_styles.addButton(self.rb_style_plastic)
        self.horizontal_layout_styles.addWidget(self.rb_style_plastic)

        self.rb_style_flat = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_style_flat.setFont(simple_font)
        self.rb_style_flat.setText("Flat")
        self.rb_group_styles.addButton(self.rb_style_flat)
        self.horizontal_layout_styles.addWidget(self.rb_style_flat)

        self.rb_style_flat_square = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_style_flat_square.setFont(simple_font)
        self.rb_style_flat_square.setText("Flat Square")
        self.rb_style_flat_square.setChecked(True)
        self.rb_group_styles.addButton(self.rb_style_flat_square)
        self.horizontal_layout_styles.addWidget(self.rb_style_flat_square)

        self.rb_style_for_badge = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_style_for_badge.setFont(simple_font)
        self.rb_style_for_badge.setText("For the Badge")
        self.rb_group_styles.addButton(self.rb_style_for_badge)
        self.horizontal_layout_styles.addWidget(self.rb_style_for_badge)

        self.rb_style_social = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_style_social.setFont(simple_font)
        self.rb_style_social.setText("Social")
        self.rb_group_styles.addButton(self.rb_style_social)
        self.horizontal_layout_styles.addWidget(self.rb_style_social)

        self.vertical_layout.addLayout(self.horizontal_layout_styles)

        ## Colors
        self.rb_group_colors = QtWidgets.QButtonGroup(frame)
        self.rb_group_colors.buttonClicked.connect(self.toggle_tf_other_enable)

        self.label_colors = QtWidgets.QLabel(self.vertical_layout_widget)
        self.label_colors.setFont(bold_font)
        self.label_colors.setText("Colors")
        self.label_colors.setAlignment(QtCore.Qt.AlignCenter)
        self.vertical_layout.addWidget(self.label_colors)

        self.rb_color_brightgreen = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_color_brightgreen.setFont(simple_font)
        self.rb_color_brightgreen.setText("Brightgreen")
        self.rb_group_colors.addButton(self.rb_color_brightgreen)
        self.horizontal_layout_colors.addWidget(self.rb_color_brightgreen)

        self.rb_color_green = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_color_green.setFont(simple_font)
        self.rb_color_green.setText("Green")
        self.rb_group_colors.addButton(self.rb_color_green)
        self.horizontal_layout_colors.addWidget(self.rb_color_green)

        self.rb_color_yellowgreen = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_color_yellowgreen.setFont(simple_font)
        self.rb_color_yellowgreen.setText("Yellowgreen")
        self.rb_group_colors.addButton(self.rb_color_yellowgreen)
        self.horizontal_layout_colors.addWidget(self.rb_color_yellowgreen)

        self.rb_color_yellow = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_color_yellow.setFont(simple_font)
        self.rb_color_yellow.setText("Yellow")
        self.rb_group_colors.addButton(self.rb_color_yellow)
        self.horizontal_layout_colors.addWidget(self.rb_color_yellow)

        self.rb_color_orange = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_color_orange.setFont(simple_font)
        self.rb_color_orange.setText("Orange")
        self.rb_group_colors.addButton(self.rb_color_orange)
        self.horizontal_layout_colors.addWidget(self.rb_color_orange)

        self.rb_color_red = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_color_red.setFont(simple_font)
        self.rb_color_red.setText("Red")
        self.rb_group_colors.addButton(self.rb_color_red)
        self.horizontal_layout_colors.addWidget(self.rb_color_red)

        self.rb_color_blue = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_color_blue.setFont(simple_font)
        self.rb_color_blue.setText("Blue")
        self.rb_color_blue.setChecked(True)
        self.rb_group_colors.addButton(self.rb_color_blue)
        self.horizontal_layout_colors.addWidget(self.rb_color_blue)

        self.rb_color_lightgray = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_color_lightgray.setFont(simple_font)
        self.rb_color_lightgray.setText("Lightgray")
        self.rb_group_colors.addButton(self.rb_color_lightgray)
        self.horizontal_layout_colors.addWidget(self.rb_color_lightgray)

        self.rb_color_blueviolet = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_color_blueviolet.setFont(simple_font)
        self.rb_color_blueviolet.setText("Blueviolet")
        self.rb_group_colors.addButton(self.rb_color_blueviolet)
        self.horizontal_layout_colors.addWidget(self.rb_color_blueviolet)

        self.rb_color_other = QtWidgets.QRadioButton(self.vertical_layout_widget)
        self.rb_color_other.setFont(simple_font)
        self.rb_color_other.setText("Other:")
        self.rb_group_colors.addButton(self.rb_color_other)
        self.horizontal_layout_colors.addWidget(self.rb_color_other)

        self.tf_other_color = QtWidgets.QLineEdit(self.vertical_layout_widget)
        self.tf_other_color.setFont(simple_font)
        self.tf_other_color.setText("ff69b4")
        self.tf_other_color.setEnabled(False)
        self.tf_other_color.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontal_layout_colors.addWidget(self.tf_other_color)

        self.vertical_layout.addLayout(self.horizontal_layout_colors)

        ## Sields
        self.label_shields = QtWidgets.QLabel(self.vertical_layout_widget)
        self.label_shields.setText("Shields")
        self.label_shields.setFont(bold_font)
        self.label_shields.setAlignment(QtCore.Qt.AlignCenter)
        self.vertical_layout.addWidget(self.label_shields)

        self.cb_author = QtWidgets.QCheckBox(self.vertical_layout_widget)
        self.cb_author.setChecked(True)
        self.cb_author.setText("Author")
        self.horizontal_layout_shields.addWidget(self.cb_author)

        self.cb_last_commit = QtWidgets.QCheckBox(self.vertical_layout_widget)
        self.cb_last_commit.setChecked(True)
        self.cb_last_commit.setText("Last commit")
        self.horizontal_layout_shields.addWidget(self.cb_last_commit)

        self.cb_repo_size = QtWidgets.QCheckBox(self.vertical_layout_widget)
        self.cb_repo_size.setChecked(True)
        self.cb_repo_size.setText("Repo size")
        self.horizontal_layout_shields.addWidget(self.cb_repo_size)

        self.cb_license = QtWidgets.QCheckBox(self.vertical_layout_widget)
        self.cb_license.setChecked(True)
        self.cb_license.setText("License")
        self.horizontal_layout_shields.addWidget(self.cb_license)

        self.cb_top_language = QtWidgets.QCheckBox(self.vertical_layout_widget)
        self.cb_top_language.setChecked(True)
        self.cb_top_language.setText("Top language")
        self.horizontal_layout_shields.addWidget(self.cb_top_language)

        self.cb_num_languages = QtWidgets.QCheckBox(self.vertical_layout_widget)
        self.cb_num_languages.setChecked(True)
        self.cb_num_languages.setText("Number of languages")
        self.horizontal_layout_shields.addWidget(self.cb_num_languages)

        self.vertical_layout.addLayout(self.horizontal_layout_shields)

        ## Result
        self.label_result = QtWidgets.QLabel(self.vertical_layout_widget)
        self.label_result.setFont(bold_font)
        self.label_result.setText("Result")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.vertical_layout.addWidget(self.label_result)

        self.tf_result = QtWidgets.QPlainTextEdit(self.vertical_layout_widget)
        self.tf_result.setToolTip("Result")
        self.vertical_layout.addWidget(self.tf_result)

        self.result_view = QtWebEngineWidgets.QWebEngineView()
        self.result_view.setHtml('')
        self.vertical_layout.addWidget(self.result_view)

        ## Buttons
        self.btn_exit = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.btn_exit.setFont(bold_font)
        self.btn_exit.setToolTip("Exit aplication")
        self.btn_exit.setText("Exit")
        self.btn_exit.clicked.connect(sys.exit)
        self.horizontal_layout_buttons.addWidget(self.btn_exit)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_buttons.addItem(spacerItem)

        self.btn_copy = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.btn_copy.setFont(bold_font)
        self.btn_copy.setToolTip("Copy to Clipboard")
        self.btn_copy.setText("Copy")
        self.btn_copy.clicked.connect(self.copy_to_clipboard)
        self.horizontal_layout_buttons.addWidget(self.btn_copy)

        self.btn_ok = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.btn_ok.setFont(bold_font)
        self.btn_ok.setToolTip("Generate code Markdown")
        self.btn_ok.setText("OK")
        self.btn_ok.clicked.connect(self.result)
        self.horizontal_layout_buttons.addWidget(self.btn_ok)

        self.vertical_layout.addLayout(self.horizontal_layout_buttons)

        frame.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(frame)

    def toggle_tf_other_enable(self):
        self.tf_other_color.setEnabled('Other' in self.rb_group_colors.checkedButton().text())

    def selected_color(self):
        color = self.rb_group_colors.checkedButton().text().lower()
        if 'other' in color:  # Apply text field color to badges
            color = search(r'^([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', self.tf_other_color.text().replace('#', ''))
            if not color:  # Checks whether the text entered matches the HEX color pattern
                color = '000'
                QtWidgets.QMessageBox.question(self, 'Color error', 'Expected HEX color pattern (FFF or FFFFFF)')
            color = color.string
        return color

    def selected_style(self):
        return self.rb_group_styles.checkedButton().text().lower().replace(' ', '-')

    def result(self):
        self.tf_result.clear()
        if self.cb_author.isChecked():
            self.tf_result.appendPlainText(f'[![GitHub author](https://img.shields.io/badge/author-{self.tf_github_profile.text()}-{self.selected_color()}?style={self.selected_style()})](https://github.com/{self.tf_github_profile.text()})')
        if self.cb_last_commit.isChecked():
            self.tf_result.appendPlainText(f'[![GitHub last commit](https://img.shields.io/github/last-commit/{self.tf_github_profile.text()}/{self.tf_github_repo.text()}?color={self.selected_color()}&style={self.selected_style()})](../../commits/master)')
        if self.cb_repo_size.isChecked():
            self.tf_result.appendPlainText(f'![GitHub repo size](https://img.shields.io/github/repo-size/{self.tf_github_profile.text()}/{self.tf_github_repo.text()}?color={self.selected_color()}&style={self.selected_style()})')
        if self.cb_license.isChecked():
            self.tf_result.appendPlainText(f'[![GitHub license](https://img.shields.io/github/license/{self.tf_github_profile.text()}/{self.tf_github_repo.text()}?color={self.selected_color()}&style={self.selected_style()})](LICENSE)')
        if self.cb_top_language.isChecked():
            self.tf_result.appendPlainText(f'![GitHub top language](https://img.shields.io/github/languages/top/{self.tf_github_profile.text()}/{self.tf_github_repo.text()}?color={self.selected_color()}&style={self.selected_style()})')
        if self.cb_num_languages.isChecked():
            self.tf_result.appendPlainText(f'![GitHub count language](https://img.shields.io/github/languages/count/{self.tf_github_profile.text()}/{self.tf_github_repo.text()}?color={self.selected_color()}&style={self.selected_style()})')
        self.result_view.setHtml(markdown(self.tf_result.toPlainText()))

    def copy_to_clipboard(self):
        copy(self.tf_result.toPlainText())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frame = QtWidgets.QMainWindow()
    frame.setWindowIcon(QtGui.QIcon('./shields.io.png'))
    ui = MainUi()
    ui.setup_ui(frame)
    frame.show()
    sys.exit(app.exec_())
