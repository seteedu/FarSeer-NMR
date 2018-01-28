import numpy as np
from current.fslibs.FittingBase import FittingBase
import scipy.optimize as sciopt


class HillEquation(FittingBase):



    def equation(self, L0, Vmax, n, kd):
        """
        The Hill Equation.

        https://en.wikipedia.org/wiki/Hill_equation_(biochemistry)

        http://www.physiologyweb.com/calculators/hill_equation_interactive_graph.html
        """
        return (Vmax*L0**n)/(kd**n+L0**n)

    def log_okay(self, res, x, y, popt, pcov):
        s2w = \
        """
        Res:  {}
        xdata: {}
        ydata: {}
        ymax: {}
        K0.5: {}
        n: {}
        popt: {}
        pcov: {}
        **************************
        """.format(res,list(x),list(y),popt[0],popt[2], popt[1], popt, pcov)

        return s2w

    def results(self, res, popt, yhalf, status='okay'):
        if status == 'okay':
            row = "{},{},{},{},{},{}\n".format(
                res,
                status,
                popt[0],
                yhalf,
                popt[2],
                popt[1]
                )

            return row

        else:
            return "{},{},,,,,\n".format(res,status)

    def txt_plot(self, popt, yhalf):
        s2w = \
        """
        ymax: {:.3f}
        yhalf: {:.3f}
        K0.5: {:.3f}
        n: {:.3f}
        """.\
            format(popt[0],yhalf,popt[2],popt[1])

        return s2w


    def results_header(self):
        return "#res,fit,ymax,yhalf,kd,n\n"

    def fit_log_header(self, col):
        """Library with the different headers for the implemented functions."""

        s2w = \
            """# fitting for parameter: '{}'
            #fit performed: Hill Equation
            #(Vmax*[S]**n)/(K0.5**n+[S]**n)
            """. \
                format(col)

        return s2w

    def fit_data(self, x, y, res, xfit):
        """Workflow for fitting data with the Hill Equation."""

        p_guess = [np.max(y), 1, np.median(x)]

        try:
            popt, pcov = sciopt.curve_fit(self.equation, x, y, p0=p_guess)

        except:
            print("*** Fit residue {} - Failed!".format(res))
            a = self.fit_failed(res, x, y)
            b = self.results(res, None, None, status='failed')
            c = "fit failed"
            d = False
            e = None
            return a, b, c, d, e

        yhalf = popt[0]/2
        print("*** Fit residue {} - OK!".format(res))
        a = self.log_okay(res, x, y, popt, pcov)
        b = self.results(res, popt, yhalf)
        c = self.txt_plot(popt, yhalf)
        d = True
        e = self.equation(xfit, popt[0], popt[1], popt[2])

        return a, b, c, d, e