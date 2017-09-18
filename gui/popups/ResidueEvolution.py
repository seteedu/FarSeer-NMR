from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QGridLayout, QDialogButtonBox
from gui.components.LabelledCombobox import LabelledCombobox
from gui.components.LabelledCheckbox import LabelledCheckbox
from gui.components.LabelledDoubleSpinBox import LabelledDoubleSpinBox
from gui.components.LabelledSpinBox import LabelledSpinBox
from gui.components.LabelledLineEdit import LabelledLineEdit
from gui.components.ColourBox import ColourBox
from functools import partial
from gui.gui_utils import defaults
class ResidueEvolutionPopup(QDialog):

    def __init__(self, parent=None, variables=None, **kw):
        super(ResidueEvolutionPopup, self).__init__(parent)
        self.setWindowTitle("Residue Evolution Plot")
        grid = QGridLayout()
        grid.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(grid)
        self.variables = None
        if variables:
            self.variables = variables["res_evo_settings"]
        self.default = defaults["res_evo_settings"]

        self.res_evo_cols = LabelledSpinBox(self, text="Columns Per Page", min=1, step=1)
        self.res_evo_rows = LabelledSpinBox(self, text="Rows Per Page", min=1, step=1)
        self.res_evo_set_x_values = LabelledCheckbox(self, "Use User Defined X Values?")
        self.res_evo_x_ticks_nbins = LabelledSpinBox(self, text="Number of Ticks", min=1, step=1)
        self.res_evo_x_label = LabelledLineEdit(self, text="X Label")
        self.res_evo_plot_line_style = LabelledCombobox(self, text="Plot Line Style", items=['-', '--', '-.', ':'])
        self.res_evo_plot_line_width = LabelledSpinBox(self, 'Line Width', min=0, step=1)
        self.res_evo_line_color = ColourBox(self, text='Marker Colour')
        self.res_evo_plot_marker_style = LabelledCombobox(self, text="Plot Line Style", items=['-', '--', '-.', ':', 'o'])
        self.res_evo_plot_marker_size = LabelledSpinBox(self, 'Marker Size', min=0, step=1)
        self.res_evo_plot_fill_between = LabelledCheckbox(self, text="Draw Data Shade")
        self.res_evo_plot_fill_colour = ColourBox(self, text="Shade Colour")
        self.res_evo_fill_alpha = LabelledDoubleSpinBox(self, text="Shade Transparency", min=0, max=1, step=0.1)
        self.res_evo_fit_line_colour = ColourBox(self, text="Fit Line Colour")
        self.res_evo_fit_line_width = LabelledSpinBox(self, text="Fit Line Width", min=0, step=1)
        self.res_evo_fit_line_style = LabelledCombobox(self, text="Fit Line Style", items=['-', '--', '-.', ':', 'o'])

        self.layout().addWidget(self.res_evo_cols, 0, 0)
        self.layout().addWidget(self.res_evo_rows, 1, 0)
        self.layout().addWidget(self.res_evo_set_x_values, 2, 0)
        self.layout().addWidget(self.res_evo_x_ticks_nbins, 3, 0)
        self.layout().addWidget(self.res_evo_x_label, 4, 0)
        self.layout().addWidget(self.res_evo_plot_line_style, 5, 0)
        self.layout().addWidget(self.res_evo_plot_line_width, 6, 0)
        self.layout().addWidget(self.res_evo_line_color, 7, 0)
        self.layout().addWidget(self.res_evo_plot_marker_style, 0, 1)
        self.layout().addWidget(self.res_evo_plot_marker_size, 1, 1)
        self.layout().addWidget(self.res_evo_plot_fill_between, 2, 1)
        self.layout().addWidget(self.res_evo_plot_fill_colour, 3, 1)
        self.layout().addWidget(self.res_evo_fill_alpha, 4, 1)
        self.layout().addWidget(self.res_evo_fit_line_colour, 5, 1)
        self.layout().addWidget(self.res_evo_fit_line_width, 6, 1)
        self.layout().addWidget(self.res_evo_fit_line_style, 7, 1)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel | QDialogButtonBox.RestoreDefaults)

        self.buttonBox.accepted.connect(partial(self.set_values, variables))
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.button(QDialogButtonBox.RestoreDefaults).clicked.connect(self.get_defaults)

        self.layout().addWidget(self.buttonBox, 8, 0, 1, 2)

        if variables:
            self.get_values()

    def get_defaults(self):
        self.res_evo_cols.setValue(self.default["cols_page"])
        self.res_evo_rows.setValue(self.default["rows_page"])
        self.res_evo_set_x_values.setChecked(self.default["set_x_values"])
        self.res_evo_x_ticks_nbins.setValue(self.default["x_ticks_nbins"])
        self.res_evo_x_label.field.setText(self.default["x_label"])
        self.res_evo_plot_line_style.select(self.default["line_style"])
        self.res_evo_plot_line_width.setValue(self.default["line_width"])
        self.res_evo_line_color.select(self.default["line_color"])
        self.res_evo_plot_marker_style.select(self.default["marker_style"])
        self.res_evo_plot_marker_size.setValue(self.default["marker_size"])
        self.res_evo_plot_fill_between.setChecked(self.default["fill_between"])
        self.res_evo_plot_fill_colour.select(self.default["fill_color"])
        self.res_evo_fill_alpha.setValue(self.default["fill_alpha"])
        self.res_evo_fit_line_colour.select(self.default["fit_line_color"])
        self.res_evo_fit_line_width.setValue(self.default["fit_line_width"])
        self.res_evo_fit_line_style.select(self.default["fit_line_style"])

    def set_values(self, variables):
        self.variables["cols_page"] = self.res_evo_cols.field.value()
        self.variables["rows_page"] = self.res_evo_rows.field.value()
        self.variables["set_x_values"] = self.res_evo_set_x_values.checkBox.isChecked()
        self.variables["x_ticks_nbins"] = self.res_evo_x_ticks_nbins.field.value()
        self.variables["x_label"] = self.res_evo_x_label.field.text()
        self.variables["line_style"] = self.res_evo_plot_line_style.fields.currentText()
        self.variables["line_width"] = self.res_evo_plot_line_width.field.value()
        self.variables["line_color"] = self.res_evo_line_color.fields.currentText()
        self.variables["marker_style"] = self.res_evo_plot_marker_style.fields.currentText()
        self.variables["marker_size"] = self.res_evo_plot_marker_size.field.value()
        self.variables["fill_between"] = self.res_evo_plot_fill_between.checkBox.isChecked()
        self.variables["fill_color"] = self.res_evo_plot_fill_colour.fields.currentText()
        self.variables["fill_alpha"] = self.res_evo_fill_alpha.field.value()
        self.variables["fit_line_color"] = self.res_evo_fit_line_colour.fields.currentText()
        self.variables["fit_line_width"] = self.res_evo_fit_line_width.field.value()
        self.variables["fit_line_style"] = self.res_evo_fit_line_style.fields.currentText()
        variables["res_evo_settings"] = self.variables
        self.accept()

    def get_values(self):
        self.res_evo_cols.setValue(self.variables["cols_page"])
        self.res_evo_rows.setValue(self.variables["rows_page"])
        self.res_evo_set_x_values.setChecked(self.variables["set_x_values"])
        self.res_evo_x_ticks_nbins.setValue(self.variables["x_ticks_nbins"])
        self.res_evo_x_label.field.setText(self.variables["x_label"])
        self.res_evo_plot_line_style.select(self.variables["line_style"])
        self.res_evo_plot_line_width.setValue(self.variables["line_width"])
        self.res_evo_line_color.select(self.variables["line_color"])
        self.res_evo_plot_marker_style.select(self.variables["marker_style"])
        self.res_evo_plot_marker_size.setValue(self.variables["marker_size"])
        self.res_evo_plot_fill_between.setChecked(self.variables["fill_between"])
        self.res_evo_plot_fill_colour.select(self.variables["fill_color"])
        self.res_evo_fill_alpha.setValue(self.variables["fill_alpha"])
        self.res_evo_fit_line_colour.select(self.variables["fit_line_color"])
        self.res_evo_fit_line_width.setValue(self.variables["fit_line_width"])
        self.res_evo_fit_line_style.select(self.variables["fit_line_style"])
