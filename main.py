from ply_parser import latex_to_html
from html_output import save_html_to_file

latex_input = r"""
\sqrt{x} \\ 
\sqrt[3]{y} + \int_{0}^{1} x^{2} dx \\ 
\iint_{0}^{1} x^{2} dx dy \\ 
\iiint_{0}^{1} x^{2} dx dy dz \\ 
\frac{1}{2} + \sum_{n=1}^{10} n^{2} \\ 
\alpha + \beta + \gamma + \Delta + \pi \\ 
x \geq y \\ 
x \leq y \\ 
x \neq y \\ 
x \in A \\ 
x \notin A \\ 
\forall x \exists y \\ 
\left( x + \frac{1}{2} \right) \\ 
\left[ \sqrt{y} \right] \\ 
\left\{ \int_{0}^{1} x dx \right\} \\ 
\log{x} + \log_{2}{x} + \ln{x}
"""

html_output = latex_to_html(latex_input)
save_html_to_file(html_output)
