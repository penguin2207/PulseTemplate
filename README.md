<div class="document">

<div class="documentwrapper">

<div class="bodywrapper">

<div class="body" role="main">

<div class="section" id="documentation-for-pulsepy">

# [Documentation for PulsePy](#id1)[¶](#documentation-for-pulsepy "Permalink to this headline")

<div class="contents topic" id="contents">

Contents

*   [Documentation for PulsePy](#documentation-for-pulsepy)
    *   [Introduction](#introduction)
    *   [requirements.txt](#requirements-txt)
    *   [ScopeTrace.py](#module-ScopeTrace)
    *   [ScopeData.py](#module-ScopeData)
    *   [ScopeTrace.py](#module-ScopeTrace)
    *   [PulseTemplate.py](#module-PulseTemplate)

</div>

<div class="section" id="introduction">

## [Introduction](#id2)[¶](#introduction "Permalink to this headline")

‘PulsePy' is a tool designed to facilitate the analysis of pulses. This package can create a Landau curve or a template curve that best fits existing pulses and simulate new pulses. PulsePy is divided into three classes and a function: ScopeTrace, ScopeData, PulseTemplate and SimiulatePulses. ScopeTrace can identify x and y values from a CSV file and calculate baseline and jitter values, which correspond to the mean value and variance. With those values, the class can also convert and plot y values to facilitate the visualization of both the observed data and Landau fit curve. ScopeTrace can also create the best fit of the observed pulse in the Landau distribution function using the curvefit function in pylandau package with three parameters: mpv, eta, and A. These three parameters each depends on the the x value of the peak, width, and amplitude of the pulse. The quality of a fitted function is determined based on the proximity of initial guess parameters to actual working parameters that have decent fits.

ScopeData allows users to store parameters and search for pulses that meet specific requirements. The function simulate_pulses allows users to simulate pulses with customized conditions provided by users.

PulseTemplate takes a given template or generates a custom one from data and uses that curve to fit to given function.

To run this package, the following packages should be installed: sys, os, pylandau, numpy, matplotlib, scipy, itertools, random, time, csv

There are two options to install these packages. The first option is: type in ‘pip install <package>’ in linux command line. Below is an exmple of how to install a package using Linux.

<div class="highlight-default notranslate">

<div class="highlight">

<pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="n">sys</span> <span class="n">os</span> <span class="n">pylandau</span> <span class="n">numpy</span> <span class="c1">#List all the required packages that are not already installed into your system with a space in between each name.</span>
</pre>

</div>

</div>

The second option is:

<div class="highlight-default notranslate">

<div class="highlight">

<pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre>

</div>

</div>

‘’‘

</div>

<div class="section" id="requirements-txt">

## [requirements.txt](#id3)[¶](#requirements-txt "Permalink to this headline")

</div>

<div class="section" id="module-ScopeTrace"><span id="scopetrace-py"></span>

## [ScopeTrace.py](#id4)[¶](#module-ScopeTrace "Permalink to this headline")

<dl class="class">

<dt id="ScopeTrace.ScopeTrace">_class_ `ScopeTrace.``ScopeTrace`<span class="sig-paren">(</span>_data='15192.CSV'_, _n_average=1_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace)[¶](#ScopeTrace.ScopeTrace "Permalink to this definition")</dt>

<dd>

This is a class to manage a oscilloscope trace.

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.get_trigger_point">`get_trigger_point`<span class="sig-paren">(</span><span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.get_trigger_point)[¶](#ScopeTrace.ScopeTrace.get_trigger_point "Permalink to this definition")</dt>

<dd>

Returns an x value where the pulse was triggered.

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.get_xmin">`get_xmin`<span class="sig-paren">(</span><span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.get_xmin)[¶](#ScopeTrace.ScopeTrace.get_xmin "Permalink to this definition")</dt>

<dd>

Returns a minimum x value from the data.

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.get_xmax">`get_xmax`<span class="sig-paren">(</span><span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.get_xmax)[¶](#ScopeTrace.ScopeTrace.get_xmax "Permalink to this definition")</dt>

<dd>

Returns a maximum x value from the data.

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.find_baseline_and_jitter">`find_baseline_and_jitter`<span class="sig-paren">(</span>_xmin_, _xmax_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.find_baseline_and_jitter)[¶](#ScopeTrace.ScopeTrace.find_baseline_and_jitter "Permalink to this definition")</dt>

<dd>

Finds a baseline and a jitter value, which correspond to a mean value and variance.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **xmin** (_float_) – X minimum value.
*   **xmax** (_float_) – X maximum value.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.find_value">`find_value`<span class="sig-paren">(</span>_name_, _type='f'_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.find_value)[¶](#ScopeTrace.ScopeTrace.find_value "Permalink to this definition")</dt>

<dd>

Returns the oscilloscope settings such as record length, sample interval, units, etc.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **name** (_str_) – Name of value of interest, such as ‘Trigger Point’.
*   **data** (_str_) – Read CSV file. Compatible with ScopeData.ScopeData.data_read().
*   **type** (_'f'/'i'/optional_) – Type of values evaluated. ‘f’ for float and ‘i’ for integer or index.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.inverted">`inverted`<span class="sig-paren">(</span><span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.inverted)[¶](#ScopeTrace.ScopeTrace.inverted "Permalink to this definition")</dt>

<dd>

Returns a list of y values of which baseline has been reset to zero and then are reflected about the x-axis.

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.fwhm">`fwhm`<span class="sig-paren">(</span><span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.fwhm)[¶](#ScopeTrace.ScopeTrace.fwhm "Permalink to this definition")</dt>

<dd>

Returns an approximated full width at half maximum.

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.get_num_pulses">`get_num_pulses`<span class="sig-paren">(</span><span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.get_num_pulses)[¶](#ScopeTrace.ScopeTrace.get_num_pulses "Permalink to this definition")</dt>

<dd>

Returns the number of pulses of a file.

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.parameters">`parameters`<span class="sig-paren">(</span>_yvals=None_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.parameters)[¶](#ScopeTrace.ScopeTrace.parameters "Permalink to this definition")</dt>

<dd>

Suppresses warning messages that do not affect the results of a Landau fitting method. Finds parameters of a landau distribution fit.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">**yvals** (_list/None_) – List of parameters, mpv, eta, amp, for a landau fitting curve.</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.plot">`plot`<span class="sig-paren">(</span>_fit_param=None_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.plot)[¶](#ScopeTrace.ScopeTrace.plot "Permalink to this definition")</dt>

<dd>

Plots trace data with optional Landau fit.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">**fit_param** (_array/None/optional_) – Array of Landau parameters: mpv, eta, and amp.</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.plot_range">`plot_range`<span class="sig-paren">(</span>_xmin_, _xmax_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.plot_range)[¶](#ScopeTrace.ScopeTrace.plot_range "Permalink to this definition")</dt>

<dd>

Plots trace with given ranges.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **xmin** (_integer_) – Minimum x (by index).
*   **xmax** (_integer_) – Maximum x (by index).

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.addPlot">`addPlot`<span class="sig-paren">(</span>_xValues_, _yValues_, _label_, _color='b-'_, _alpha=1._<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.addPlot)[¶](#ScopeTrace.ScopeTrace.addPlot "Permalink to this definition")</dt>

<dd>

Adds a plot to current window with specified attributes.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **xValues** (_numpy array_) – X values of data to be plotted.
*   **yValues** (_numpy array_) – Y values of data to be plotted.
*   **label** (_str_) – Label of data on graph.
*   **color='b-'** (_str_) – Color of data, default is blue.
*   **alpha=1.** (_float_) – Transparency of data, default is opaque.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.pulseFromFile">`pulseFromFile`<span class="sig-paren">(</span>__dir_, _filename_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.pulseFromFile)[¶](#ScopeTrace.ScopeTrace.pulseFromFile "Permalink to this definition")</dt>

<dd>

Creates a scope trace object from given attributes.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **_dir** (_str_) – Directory of pulse data.
*   **filename** (_str_) – Filename of pulse data.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.saveFig">`saveFig`<span class="sig-paren">(</span>_filename_,_xValues_, _yValues_, _outputDir=None_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.saveFig)[¶](#ScopeTrace.ScopeTrace.saveFig "Permalink to this definition")</dt>

<dd>

Stores data as a plot.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **filename** (_str_) – Name of output file.
*   **xValues** (_numpy array_) – X values of data to be saved.
*   **yValues** (_numpy array_) – Y values of data to be saved.
*   **outputDir** (_str_) – Directory to save file, default is in the DataDir directory.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.saveFile">`saveFile`<span class="sig-paren">(</span>_filename_,_xValues_, _yValues_, _outputDir=None_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.saveFile)[¶](#ScopeTrace.ScopeTrace.saveFile "Permalink to this definition")</dt>

<dd>

Stores data as either a csv file.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **filename** (_str_) – Name of output file.
*   **xValues** (_numpy array_) – X values of data to be saved.
*   **yValues** (_numpy array_) – Y values of data to be saved.
*   **outputDir** (_str_) – Directory to save file, default is in the DataDir directory.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.plotFinish">`plotFinish`<span class="sig-paren">(</span>_filename_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.plotFinish)[¶](#ScopeTrace.ScopeTrace.plotFinish "Permalink to this definition")</dt>

<dd>

Saves all added plots in specified directory from saveFig with user specified name and clears window.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **filename** (_str_) – Filename of final plot.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="ScopeTrace.ScopeTrace.pulses">`pulses`<span class="sig-paren">(</span>_pulseDir_, _template_, _genDir=(dataPath+'/genPulses/Pulses/'))_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeTrace.html#ScopeTrace.pulses)[¶](#ScopeTrace.ScopeTrace.pulses "Permalink to this definition")</dt>

<dd>

Plots trace with given ranges.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **pulseDir** (_str_) – Directory where pulses to be fitted can be found.
*   **template** (_Template Object_) – Template Object to fit to pulses.
*   **genDir** (_str_) – Directory where generated pulse graphs are stored.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

</dd>

</dl>

</div>

<div class="section" id="module-PulseTemplate"><span id="pulsetemplate-py"></span>

## [PulseTemplate.py](#id7)[¶](#module-PulseTemplate "Permalink to this headline")

<dl class="class">

<dt id="PulseTemplate.PulseTemplate">_class_ `PulseTemplate.``PulseTemplate`<span class="sig-paren">(</span><span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/PulseTemplate.html#PulseTemplate)[¶](#PulseTemplate.PulseTemplate "Permalink to this definition")</dt>

<dd>

This class manages pulse templates.

<dl class="method">

<dt id="PulseTemplate.PulseTemplate.residuals">`residuals`<span class="sig-paren">(</span>_templateData_, _rawData_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/PulseTemplate.html#PulseTemplate.residuals)[¶](#PulseTemplate.PulseTemplate.residuals "Permalink to this definition")</dt>

<dd>

Subtracts template data from raw data, returns resulting array.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **templateData** (_numpy array_) – Y values of template data.
*   **rawData** (_numpy array_) – Y values of raw data.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="PulseTemplate.PulseTemplate.makeTemp">`makeTemp`<span class="sig-paren">(</span>_templatePath=None_, _templateName=None_,_targetDir=None_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/PulseTemplate.html#PulseTemplate.makeTemp)[¶](#PulseTemplate.PulseTemplate.makeTemp "Permalink to this definition")</dt>

<dd>

Creates new template from specified directory, otherwise uses a default template.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **templatePath** (_string_) – Path of data to be made into template.
*   **templateName** (_string_) – Name of new template.
*   **targetDir** (_string_) – Location of new template to be stored.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="PulseTemplate.PulseTemplate.shiftPulses">`shiftPulses`<span class="sig-paren">(</span>_pulse_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/PulseTemplate.html#PulseTemplate.shiftPulses)[¶](#PulseTemplate.PulseTemplate.shiftPulses "Permalink to this definition")</dt>

<dd>

Takes peak value position into account. Returns x and y arrays of new data. Scales templates to data.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **pulse** (_ScopeData object_) – Pulse which will have the template scaled to.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

</dd>

</dl>

</div>

<div class="section" id="module-ScopeData"><span id="scopedata-py"></span>

## [ScopeData.py](#id5)[¶](#module-ScopeData "Permalink to this headline")

<dl class="class">

<dt id="ScopeData.ScopeData">_class_ `ScopeData.``ScopeData`<span class="sig-paren">(</span>_trace_folder_dir_, _param_dir=None_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeData.html#ScopeData)[¶](#ScopeData.ScopeData "Permalink to this definition")</dt>

<dd>

This is a class to manage a set of ScopeTrace objects.

<dl class="method">

<dt id="ScopeData.ScopeData.data_read">`data_read`<span class="sig-paren">(</span>_filename_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeData.html#ScopeData.data_read)[¶](#ScopeData.ScopeData.data_read "Permalink to this definition")</dt>

<dd>

Returns ScopeTrace object from filename. :param str filename: String of filename.

</dd>

</dl>

<dl class="method">

<dt id="ScopeData.ScopeData.save_parameters">`save_parameters`<span class="sig-paren">(</span>_output_dir=None_, _filename=None_, _plotting=False_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeData.html#ScopeData.save_parameters)[¶](#ScopeData.ScopeData.save_parameters "Permalink to this definition")</dt>

<dd>

Saves parameters.

<div class="highlight-default notranslate">

<div class="highlight">

<pre><span></span><span class="c1">#Type in the name of the directory where the data files are stored</span> 
<span class="kn">import</span> <span class="nn">os</span><span class="o">,</span> <span class="nn">ScopeData</span>
<span class="n">directory</span> <span class="o">=</span> <span class="o"><</span><span class="n">PATH</span><span class="o">></span> <span class="c1">#e.g. "/home/kpark1/Work/SLab/data/"</span> 
<span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">directory</span><span class="p">)):</span>
    <span class="n">f</span> <span class="o">=</span> <span class="n">ScopeData</span><span class="o">.</span><span class="n">ScopeData</span><span class="p">(</span><span class="n">directory</span><span class="p">)</span>
    <span class="n">f</span><span class="o">.</span><span class="n">data_read</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="n">f</span><span class="o">.</span><span class="n">save_parameters</span><span class="p">(</span><span class="n">plotting</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span>
</pre>

</div>

</div>

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **output_dir** (_str/None/optional_) – Directory for storing Landau fit parameters: mpv, eta, amp, and jitter (variance). The default directory is working directory.
*   **filename** (_str/None/optional_) – Name of a new saved csv files that ends with ‘.csv’. If None, then the function creates a filename based on the trace folder title.
*   **plotting** (_bool/optional_) – If True, it plots each fitted curve. If False, it does not generate any graphs.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="ScopeData.ScopeData.search_pulses">`search_pulses`<span class="sig-paren">(</span>_conditions_, _parameters_, _and_or='and'_, _plotting=True_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeData.html#ScopeData.search_pulses)[¶](#ScopeData.ScopeData.search_pulses "Permalink to this definition")</dt>

<dd>

Returns a list of files that satisfy conditions from a user input with an option of plotting the pulses. Requires a directory where parameters have already been saved.

<div class="highlight-default notranslate">

<div class="highlight">

<pre><span></span><span class="c1">#Type in the name of the directory where the data files are stored and the output directory</span>
<span class="kn">import</span> <span class="nn">ScopeData</span>
<span class="n">directory</span> <span class="o">=</span>  <span class="o"><</span><span class="n">PATH</span><span class="o">></span> <span class="c1">#e.g. "/home/kpark1/Work/SLab/data/"</span>
<span class="n">f</span> <span class="o">=</span> <span class="n">ScopeData</span><span class="o">.</span><span class="n">ScopeData</span><span class="p">(</span><span class="n">directory</span><span class="p">)</span>
<span class="n">f</span><span class="o">.</span><span class="n">save_parameters</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">search_pulses</span><span class="p">([</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span> <span class="o"><</span> <span class="o">.</span><span class="mi">002</span><span class="p">,</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span> <span class="o"><</span> <span class="o">.</span><span class="mi">004</span><span class="p">],</span>
                      <span class="p">[</span><span class="s1">'amp'</span><span class="p">,</span> <span class="s1">'mpv'</span><span class="p">],</span> <span class="n">plotting</span> <span class="o">=</span> <span class="kc">False</span><span class="p">))</span>
</pre>

</div>

</div>

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **conditions** (_list_) – List of boolean functions.
*   **parameters** (_list_) – List of parameters [mpv, eta, amp] to check if the conditions apply to them. The list must have the same length as conditions.
*   **and_or** (_str/optional_) – String of either ‘and’ or ‘or’. If the input is ‘and’, the method returns files that meet all of the given conditions. If the input is ‘or’, it returns files that meet any of the conditions.
*   **plotting** (_bool/optional_) – If True, it plots the pulses from the data.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="method">

<dt id="ScopeData.ScopeData.histogram">`histogram`<span class="sig-paren">(</span>_parameter_, _hbins=10_, _hrange=None_, _hcolor='r'_, _hedgecolor='k'_, _halpha=0.5_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/ScopeData.html#ScopeData.histogram)[¶](#ScopeData.ScopeData.histogram "Permalink to this definition")</dt>

<dd>

Makes a histogram of parameters. Returns a list parameters, a mean value and standard deviation, of Gaussian fit to histogram if parameter == ‘eta’ or ‘jitter’:

<div class="highlight-default notranslate">

<div class="highlight">

<pre><span></span><span class="kn">import</span> <span class="nn">ScopeData</span>
<span class="n">directory</span> <span class="o">=</span> <span class="o"><</span><span class="n">PATH</span><span class="o">></span> <span class="s2">"/home/$USERNAME/Work/SLab/data/"</span>
<span class="n">f</span> <span class="o">=</span> <span class="n">ScopeData</span><span class="o">.</span><span class="n">ScopeData</span><span class="p">(</span><span class="n">directory</span><span class="p">)</span>
<span class="n">f</span><span class="o">.</span><span class="n">histogram</span><span class="p">(</span><span class="s1">'jitter'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre>

</div>

</div>

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **parameter** (_string_) – Name of parameters among jitter, eta, mpv, and amp.
*   **hbins** (_integer/optional_) – Number of bins.
*   **hrange** (_list/optional_) – Histogram Range
*   **hcolor** (_string/optional_) – Color of histogram bins
*   **hedgecolor** (_string/optional_) – Color of edges of the bins
*   **halpha** (_float/optional_) – Level of transparency in color of bins

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

</dd>

</dl>

</div>

<div class="section" id="module-SimulatePulses"><span id="simulatepulses-py"></span>

## [SimulatePulses.py](#id6)[¶](#module-SimulatePulses "Permalink to this headline")

<dl class="function">

<dt id="SimulatePulses.fwhm">`SimulatePulses.``fwhm`<span class="sig-paren">(</span>_x_, _y_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/SimulatePulses.html#fwhm)[¶](#SimulatePulses.fwhm "Permalink to this definition")</dt>

<dd>

Finds an approximate full width half maximum. :param list x: List of x values. :param list y: List of y values.

</dd>

</dl>

<dl class="function">

<dt id="SimulatePulses.gaus">`SimulatePulses.``gaus`<span class="sig-paren">(</span>_x_, _a_, _x0_, _sigma_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/SimulatePulses.html#gaus)[¶](#SimulatePulses.gaus "Permalink to this definition")</dt>

<dd>

Defines a gaussian function.

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **x** (_list_) – List of values.
*   **a** (_float_) – Amplitude of the function.
*   **x0** (_float_) – Expected value.
*   **sigma** (_float_) – Sigma value.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

<dl class="function">

<dt id="SimulatePulses.simulate_pulses">`SimulatePulses.``simulate_pulses`<span class="sig-paren">(</span>_num_events=2, time_range=array([0.00000000e+00, 8.00320128e-10, 1.60064026e-09, ..., 1.99839936e-06, 1.99919968e-06, 2.00000000e-06]), eta_stats=[5e-08, 0], amp_stats=[0.1, 0], jitter_stats=[2e-06, 0], trigger_threshold=None, baseline=0.0, trigger_offset=None, num_pulses=None, possion_parameter=1, plotting=False, plot_pulse=False, save=True, output_dir=None_<span class="sig-paren">)</span>[<span class="viewcode-link">[source]</span>](_modules/SimulatePulses.html#simulate_pulses)[¶](#SimulatePulses.simulate_pulses "Permalink to this definition")</dt>

<dd>

Simulates Landau pulses with noise or jitter. Returns ScopeData object.

<div class="highlight-default notranslate">

<div class="highlight">

<pre><span></span><span class="kn">import</span> <span class="nn">SimulatePulses</span>
<span class="n">SimulatePulses</span><span class="o">.</span><span class="n">simulate_pulses</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mf">2e-06</span><span class="p">,</span> <span class="mi">2500</span><span class="p">),</span> 
                         <span class="p">[</span><span class="mf">5e-08</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span> <span class="p">,[</span><span class="mf">1e-01</span><span class="p">,</span><span class="mi">0</span><span class="p">],[</span><span class="mf">2e-06</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span> 
                         <span class="n">plotting</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">plot_pulse</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
 <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre>

</div>

</div>

<table class="docutils field-list" frame="void" rules="none"><colgroup><col class="field-name"> <col class="field-body"></colgroup>

<tbody valign="top">

<tr class="field-odd field">

<th class="field-name">Parameters:</th>

<td class="field-body">

*   **num_events** (_integer_) – Number of files of events to create.
*   **time_range** (_array_) – Time range (x axis) for simulation.
*   **eta_stats** (_list_) – List containing a mean value and a standard deviation of eta values of pulses: ([mean value, std dev]).
*   **jitter_stats** (_list_) – List containing a mean value and a standard deviation of jitter (variance) of data: ([mean value, std dev]).
*   **amp_stats** (_list_) – List containing lower and upper bounds of amplitude over a random distribution: ([min, max]).
*   **trigger_threshold** (_bool/optional_) – Simulates an oscilloscope trigger threshold. The first pulse of which amplitude is equal to or greater than the trigger threshold will be found at the trigger offset. If None, it simulates a random scope window.
*   **baseline** (_float/optional_) – Sets a baseline voltage.
*   **trigger_offset** (_float/optional_) – X value of a triggered spot; If trigger_offset == None, the default trigger offset is 1/10 of the time range.
*   **num_pulses** (_integer/optional_) – Number of pulses per event. If None, the number is picked randomly from poisson distribution.
*   **possion_parameter** (_float/optional_) – Number of pulses randomly picked based on Possion Distribution.
*   **plotting** (_bool/optional_) – If True, it plots the simulated pulse.
*   **plot_pulse** (_bool/optional_) – If True, it plots landau pulses.
*   **save** (_bool/optional_) – If True, it saves the pulse simulation in the output directory.
*   **output_dir** (_str/optional_) – Directory to a folder for the saved csv files. If None, it saves the csv files in a newly created folder in working directory.

</td>

</tr>

</tbody>

</table>

</dd>

</dl>

</div>

</div>

</div>

</div>

</div>

<div class="sphinxsidebar" role="navigation" aria-label="main navigation">

<div class="sphinxsidebarwrapper">

### [Table Of Contents](index.html)

*   [Documentation for PulsePy](#)
    *   [Introduction](#introduction)
    *   [requirements.txt](#requirements-txt)
    *   [ScopeTrace.py](#module-ScopeTrace)
    *   [ScopeData.py](#module-ScopeData)
    *   [SimulatePulses.py](#module-SimulatePulses)
    *   [SimulatePulses.py](#module-SimulatePulses)

<div class="relations">

### Related Topics

*   [Documentation overview](index.html)
    *   Previous: [Documentation for PulsePy](index.html "previous chapter")
    *   Next: [Documentation for Installing CentOS](Install_comp.html "next chapter")

</div>

<div role="note" aria-label="source link">

### This Page

*   [Show Source](_sources/PulsePy.rst.txt)

</div>

<div id="searchbox" style="display: none" role="search">

### Quick search

<div class="searchformwrapper">

<form class="search" action="search.html" method="get"><input type="text" name="q"> <input type="submit" value="Go"> <input type="hidden" name="check_keywords" value="yes"> <input type="hidden" name="area" value="default"></form>

</div>

</div>

<script type="text/javascript">$('#searchbox').show(0);</script></div>

</div>

</div>

<div class="footer">©2018, Kiryeong Park. | Powered by [Sphinx 1.7.5](http://sphinx-doc.org/) & [Alabaster 0.7.11](https://github.com/bitprophet/alabaster) | [Page source](_sources/PulsePy.rst.txt)</div>
