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
<h2><a class="toc-backref" href="#id2">Introduction</a><a class="headerlink" href="#introduction" title="Permalink to this headline">¶</a></h2>
<p>‘PulsePy' is a tool designed to facilitate the analysis of pulses. This package can create a Landau curve or a template curve that best fits existing pulses and simulate new pulses. PulsePy is divided into three classes and a function: ScopeTrace, ScopeData, PulseTemplate and SimiulatePulses.
ScopeTrace can identify x and y values from a CSV file and calculate baseline and jitter values, which correspond to the mean value and variance. With those values, the class can also convert and plot y values to facilitate the visualization of both the observed data and Landau fit curve. ScopeTrace can also create the best fit of the observed pulse in the Landau distribution function using the curvefit function in pylandau package with three parameters: mpv, eta, and A. These three parameters each depends on the the x value of the peak, width, and amplitude of the pulse. The quality of a fitted function is determined based on the proximity of initial guess parameters to actual working parameters that have decent fits.</p>
<p>ScopeData allows users to store parameters and search for pulses that meet specific requirements. The function simulate_pulses allows users to simulate pulses with customized conditions provided by users.</p>
<p>PulseTemplate takes a given template or generates a custom one from data and uses that curve to fit to given function.
</p>
<p>To run this package, the following packages should be installed:
sys, os, pylandau, numpy, matplotlib, scipy, itertools, random, time, csv</p>
<p>There are two options to install these packages. The first option is: type in ‘pip install &lt;package&gt;’ in linux command line. Below is an exmple of how to install a package using Linux.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="n">sys</span> <span class="n">os</span> <span class="n">pylandau</span> <span class="n">numpy</span> <span class="c1">#List all the required packages that are not already installed into your system with a space in between each name.</span>
</pre></div>
</div>
<p>The second option is:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div>
</div>
<p>‘’‘</p>
</div>
<div class="section" id="requirements-txt">
<h2><a class="toc-backref" href="#id3">requirements.txt</a><a class="headerlink" href="#requirements-txt" title="Permalink to this headline">¶</a></h2>
</div>
<div class="section" id="module-ScopeTrace">
<span id="scopetrace-py"></span><h2><a class="toc-backref" href="#id4">ScopeTrace.py</a><a class="headerlink" href="#module-ScopeTrace" title="Permalink to this headline">¶</a></h2>
<dl class="class">
<dt id="ScopeTrace.ScopeTrace">
<em class="property">class </em><code class="descclassname">ScopeTrace.</code><code class="descname">ScopeTrace</code><span class="sig-paren">(</span><em>data='15192.CSV'</em>, <em>n_average=1</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace" title="Permalink to this definition">¶</a></dt>
<dd><p>This is a class to manage a oscilloscope trace.</p>
<dl class="method">
<dt id="ScopeTrace.ScopeTrace.get_trigger_point">
<code class="descname">get_trigger_point</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.get_trigger_point"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.get_trigger_point" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an x value where the pulse was triggered.</p>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.get_xmin">
<code class="descname">get_xmin</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.get_xmin"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.get_xmin" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a minimum x value from the data.</p>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.get_xmax">
<code class="descname">get_xmax</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.get_xmax"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.get_xmax" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a maximum x value from the data.</p>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.find_baseline_and_jitter">
<code class="descname">find_baseline_and_jitter</code><span class="sig-paren">(</span><em>xmin</em>, <em>xmax</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.find_baseline_and_jitter"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.find_baseline_and_jitter" title="Permalink to this definition">¶</a></dt>
<dd><p>Finds a baseline and a jitter value, which correspond to a mean value and variance.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>xmin</strong> (<em>float</em>) – X minimum value.</li>
<li><strong>xmax</strong> (<em>float</em>) – X maximum value.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.find_value">
<code class="descname">find_value</code><span class="sig-paren">(</span><em>name</em>, <em>type='f'</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.find_value"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.find_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the oscilloscope settings such as record length, sample interval, units, etc.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>name</strong> (<em>str</em>) – Name of value of interest, such as ‘Trigger Point’.</li>
<li><strong>data</strong> (<em>str</em>) – Read CSV file. Compatible with ScopeData.ScopeData.data_read().</li>
<li><strong>type</strong> (<em>'f'/'i'/optional</em>) – Type of values evaluated. ‘f’ for float and ‘i’ for integer or index.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.inverted">
<code class="descname">inverted</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.inverted"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.inverted" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a list of y values of which baseline has been reset to zero and then are reflected about the x-axis.</p>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.fwhm">
<code class="descname">fwhm</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.fwhm"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.fwhm" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an approximated full width at half maximum.</p>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.get_num_pulses">
<code class="descname">get_num_pulses</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.get_num_pulses"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.get_num_pulses" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the number of pulses of a file.</p>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.parameters">
<code class="descname">parameters</code><span class="sig-paren">(</span><em>yvals=None</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.parameters"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Suppresses warning messages that do not affect the results of a Landau fitting method.
Finds parameters of a landau distribution fit.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>yvals</strong> (<em>list/None</em>) – List of parameters, mpv, eta, amp, for a landau fitting curve.</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.plot">
<code class="descname">plot</code><span class="sig-paren">(</span><em>fit_param=None</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.plot"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.plot" title="Permalink to this definition">¶</a></dt>
<dd><p>Plots trace data with optional Landau fit.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>fit_param</strong> (<em>array/None/optional</em>) – Array of Landau parameters: mpv, eta, and amp.</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.plot_range">
<code class="descname">plot_range</code><span class="sig-paren">(</span><em>xmin</em>, <em>xmax</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.plot_range"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.plot_range" title="Permalink to this definition">¶</a></dt>
<dd><p>Plots trace with given ranges.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>xmin</strong> (<em>integer</em>) – Minimum x (by index).</li>
<li><strong>xmax</strong> (<em>integer</em>) – Maximum x (by index).</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.addPlot">
<code class="descname">addPlot</code><span class="sig-paren">(</span><em>xValues</em>, <em>yValues</em>, <em>label</em>, <em>color='b-'</em>, <em>alpha=1.</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.addPlot"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.addPlot" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds a plot to current window with specified attributes.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>xValues</strong> (<em>numpy array</em>) – X values of data to be plotted.</li>
<li><strong>yValues</strong> (<em>numpy array</em>) – Y values of data to be plotted.</li>
<li><strong>label</strong> (<em>str</em>) – Label of data on graph.</li>
<li><strong>color='b-'</strong> (<em>str</em>) – Color of data, default is blue.</li>
<li><strong>alpha=1.</strong> (<em>float</em>) – Transparency of data, default is opaque.</li>

</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.pulseFromFile">
<code class="descname">pulseFromFile</code><span class="sig-paren">(</span><em>_dir</em>, <em>filename</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.pulseFromFile"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.pulseFromFile" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a scope trace object from given attributes.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>_dir</strong> (<em>str</em>) – Directory of pulse data.</li>
<li><strong>filename</strong> (<em>str</em>) – Filename of pulse data.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.saveFig">
<code class="descname">saveFig</code><span class="sig-paren">(</span><em>filename</em>,<em>xValues</em>, <em>yValues</em>, <em>outputDir=None</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.saveFig"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.saveFig" title="Permalink to this definition">¶</a></dt>
<dd><p>Stores data as a plot.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>filename</strong> (<em>str</em>) – Name of output file.</li>
<li><strong>xValues</strong> (<em>numpy array</em>) – X values of data to be saved.</li>
<li><strong>yValues</strong> (<em>numpy array</em>) – Y values of data to be saved.</li>
<li><strong>outputDir</strong> (<em>str</em>) – Directory to save file, default is in the DataDir directory.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.saveFile">
<code class="descname">saveFile</code><span class="sig-paren">(</span><em>filename</em>,<em>xValues</em>, <em>yValues</em>, <em>outputDir=None</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.saveFile"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.saveFile" title="Permalink to this definition">¶</a></dt>
<dd><p>Stores data as either a csv file.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>filename</strong> (<em>str</em>) – Name of output file.</li>
<li><strong>xValues</strong> (<em>numpy array</em>) – X values of data to be saved.</li>
<li><strong>yValues</strong> (<em>numpy array</em>) – Y values of data to be saved.</li>
<li><strong>outputDir</strong> (<em>str</em>) – Directory to save file, default is in the DataDir directory.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.plotFinish">
<code class="descname">plotFinish</code><span class="sig-paren">(</span><em>filename</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.plotFinish"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.plotFinish" title="Permalink to this definition">¶</a></dt>
<dd><p>Saves all added plots in specified directory from saveFig with user specified name and clears window.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>filename</strong> (<em>str</em>) – Filename of final plot.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="ScopeTrace.ScopeTrace.pulses">
<code class="descname">pulses</code><span class="sig-paren">(</span><em>pulseDir</em>, <em>template</em>, <em>genDir=(dataPath+'/genPulses/Pulses/'))</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeTrace.html#ScopeTrace.pulses"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeTrace.ScopeTrace.pulses" title="Permalink to this definition">¶</a></dt>
<dd><p>Plots trace with given ranges.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>pulseDir</strong> (<em>str</em>) – Directory where pulses to be fitted can be found.</li>
<li><strong>template</strong> (<em>Template Object</em>) – Template Object to fit to pulses.</li>
<li><strong>genDir</strong> (<em>str</em>) – Directory where generated pulse graphs are stored.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

</div>
<div class="section" id="module-PulseTemplate">
<span id="pulsetemplate-py"></span><h2><a class="toc-backref" href="#id7">PulseTemplate.py</a><a class="headerlink" href="#module-PulseTemplate" title="Permalink to this headline">¶</a></h2>
<dl class="class">
<dt id="PulseTemplate.PulseTemplate">
<em class="property">class </em><code class="descclassname">PulseTemplate.</code><code class="descname">PulseTemplate</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="reference internal" href="_modules/PulseTemplate.html#PulseTemplate"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#PulseTemplate.PulseTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>This class manages pulse templates.</p>

<dl class="method">
<dt id="PulseTemplate.PulseTemplate.residuals">
<code class="descname">residuals</code><span class="sig-paren">(</span><em>templateData</em>, <em>rawData</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/PulseTemplate.html#PulseTemplate.residuals"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#PulseTemplate.PulseTemplate.residuals" title="Permalink to this definition">¶</a></dt>
<dd><p>Subtracts template data from raw data, returns resulting array.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>templateData</strong> (<em>numpy array</em>) – Y values of template data.</li>
<li><strong>rawData</strong> (<em>numpy array</em>) – Y values of raw data.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="PulseTemplate.PulseTemplate.makeTemp">
<code class="descname">makeTemp</code><span class="sig-paren">(</span><em>templatePath=None</em>, <em>templateName=None</em>,<em>targetDir=None</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/PulseTemplate.html#PulseTemplate.makeTemp"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#PulseTemplate.PulseTemplate.makeTemp" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates new template from specified directory, otherwise uses a default template.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>templatePath</strong> (<em>string</em>) – Path of data to be made into template.</li>
<li><strong>templateName</strong> (<em>string</em>) – Name of new template.</li>
<li><strong>targetDir</strong> (<em>string</em>) – Location of new template to be stored.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="PulseTemplate.PulseTemplate.shiftPulses">
<code class="descname">shiftPulses</code><span class="sig-paren">(</span><em>pulse</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/PulseTemplate.html#PulseTemplate.shiftPulses"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#PulseTemplate.PulseTemplate.shiftPulses" title="Permalink to this definition">¶</a></dt>
<dd><p>Takes peak value position into account. Returns x and y arrays of new data. Scales templates to data.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>pulse</strong> (<em>ScopeData object</em>) – Pulse which will have the template scaled to. </li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

</div>
<div class="section" id="module-ScopeData">
<span id="scopedata-py"></span><h2><a class="toc-backref" href="#id5">ScopeData.py</a><a class="headerlink" href="#module-ScopeData" title="Permalink to this headline">¶</a></h2>
<dl class="class">
<dt id="ScopeData.ScopeData">
<em class="property">class </em><code class="descclassname">ScopeData.</code><code class="descname">ScopeData</code><span class="sig-paren">(</span><em>trace_folder_dir</em>, <em>param_dir=None</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeData.html#ScopeData"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeData.ScopeData" title="Permalink to this definition">¶</a></dt>
<dd><p>This is a class to manage a set of ScopeTrace objects.</p>
<dl class="method">
<dt id="ScopeData.ScopeData.data_read">
<code class="descname">data_read</code><span class="sig-paren">(</span><em>filename</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeData.html#ScopeData.data_read"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeData.ScopeData.data_read" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns ScopeTrace object from filename.
:param str filename: String of filename.</p>
</dd></dl>

<dl class="method">
<dt id="ScopeData.ScopeData.save_parameters">
<code class="descname">save_parameters</code><span class="sig-paren">(</span><em>output_dir=None</em>, <em>filename=None</em>, <em>plotting=False</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeData.html#ScopeData.save_parameters"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeData.ScopeData.save_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Saves parameters.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="c1">#Type in the name of the directory where the data files are stored </span>
<span class="kn">import</span> <span class="nn">os</span><span class="o">,</span> <span class="nn">ScopeData</span>
<span class="n">directory</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">PATH</span><span class="o">&gt;</span> <span class="c1">#e.g. &quot;/home/kpark1/Work/SLab/data/&quot; </span>
<span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">directory</span><span class="p">)):</span>
    <span class="n">f</span> <span class="o">=</span> <span class="n">ScopeData</span><span class="o">.</span><span class="n">ScopeData</span><span class="p">(</span><span class="n">directory</span><span class="p">)</span>
    <span class="n">f</span><span class="o">.</span><span class="n">data_read</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="n">f</span><span class="o">.</span><span class="n">save_parameters</span><span class="p">(</span><span class="n">plotting</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span>
</pre></div>
</div>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>output_dir</strong> (<em>str/None/optional</em>) – Directory for storing Landau fit parameters: mpv, eta, amp, and jitter (variance). The default directory is working directory.</li>
<li><strong>filename</strong> (<em>str/None/optional</em>) – Name of a new saved csv files that ends with ‘.csv’. If None, then the function creates a filename based on the trace folder title.</li>
<li><strong>plotting</strong> (<em>bool/optional</em>) – If True, it plots each fitted curve. If False, it does not generate any graphs.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="ScopeData.ScopeData.search_pulses">
<code class="descname">search_pulses</code><span class="sig-paren">(</span><em>conditions</em>, <em>parameters</em>, <em>and_or='and'</em>, <em>plotting=True</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeData.html#ScopeData.search_pulses"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeData.ScopeData.search_pulses" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a list of files that satisfy conditions from a user input with an option of plotting the pulses.
Requires a directory where parameters have already been saved.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="c1">#Type in the name of the directory where the data files are stored and the output directory</span>
<span class="kn">import</span> <span class="nn">ScopeData</span>
<span class="n">directory</span> <span class="o">=</span>  <span class="o">&lt;</span><span class="n">PATH</span><span class="o">&gt;</span> <span class="c1">#e.g. &quot;/home/kpark1/Work/SLab/data/&quot;</span>
<span class="n">f</span> <span class="o">=</span> <span class="n">ScopeData</span><span class="o">.</span><span class="n">ScopeData</span><span class="p">(</span><span class="n">directory</span><span class="p">)</span>
<span class="n">f</span><span class="o">.</span><span class="n">save_parameters</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">search_pulses</span><span class="p">([</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span> <span class="o">&lt;</span> <span class="o">.</span><span class="mi">002</span><span class="p">,</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span> <span class="o">&lt;</span> <span class="o">.</span><span class="mi">004</span><span class="p">],</span>
                      <span class="p">[</span><span class="s1">&#39;amp&#39;</span><span class="p">,</span> <span class="s1">&#39;mpv&#39;</span><span class="p">],</span> <span class="n">plotting</span> <span class="o">=</span> <span class="kc">False</span><span class="p">))</span>
</pre></div>
</div>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>conditions</strong> (<em>list</em>) – List of boolean functions.</li>
<li><strong>parameters</strong> (<em>list</em>) – List of parameters [mpv, eta, amp] to check if the conditions apply to them. The list must have the same length as conditions.</li>
<li><strong>and_or</strong> (<em>str/optional</em>) – String of either ‘and’ or ‘or’. If the input is ‘and’, the method returns files that meet all of the given conditions. If the input is ‘or’, it returns files that meet any of the conditions.</li>
<li><strong>plotting</strong> (<em>bool/optional</em>) – If True, it plots the pulses from the data.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="ScopeData.ScopeData.histogram">
<code class="descname">histogram</code><span class="sig-paren">(</span><em>parameter</em>, <em>hbins=10</em>, <em>hrange=None</em>, <em>hcolor='r'</em>, <em>hedgecolor='k'</em>, <em>halpha=0.5</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/ScopeData.html#ScopeData.histogram"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#ScopeData.ScopeData.histogram" title="Permalink to this definition">¶</a></dt>
<dd><p>Makes a histogram of parameters.
Returns a list parameters, a mean value and standard deviation, of Gaussian fit to histogram if parameter == ‘eta’ or ‘jitter’:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">ScopeData</span>
<span class="n">directory</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">PATH</span><span class="o">&gt;</span> <span class="s2">&quot;/home/$USERNAME/Work/SLab/data/&quot;</span>
<span class="n">f</span> <span class="o">=</span> <span class="n">ScopeData</span><span class="o">.</span><span class="n">ScopeData</span><span class="p">(</span><span class="n">directory</span><span class="p">)</span>
<span class="n">f</span><span class="o">.</span><span class="n">histogram</span><span class="p">(</span><span class="s1">&#39;jitter&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>
</div>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>parameter</strong> (<em>string</em>) – Name of parameters among jitter, eta, mpv, and  amp.</li>
<li><strong>hbins</strong> (<em>integer/optional</em>) – Number of bins.</li>
<li><strong>hrange</strong> (<em>list/optional</em>) – Histogram Range</li>
<li><strong>hcolor</strong> (<em>string/optional</em>) – Color of histogram bins</li>
<li><strong>hedgecolor</strong> (<em>string/optional</em>) – Color of edges of the bins</li>
<li><strong>halpha</strong> (<em>float/optional</em>) – Level of transparency in color of bins</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

</div>
<div class="section" id="module-SimulatePulses">
<span id="simulatepulses-py"></span><h2><a class="toc-backref" href="#id6">SimulatePulses.py</a><a class="headerlink" href="#module-SimulatePulses" title="Permalink to this headline">¶</a></h2>
<dl class="function">
<dt id="SimulatePulses.fwhm">
<code class="descclassname">SimulatePulses.</code><code class="descname">fwhm</code><span class="sig-paren">(</span><em>x</em>, <em>y</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/SimulatePulses.html#fwhm"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#SimulatePulses.fwhm" title="Permalink to this definition">¶</a></dt>
<dd><p>Finds an approximate full width half maximum.
:param list x: List of x values.
:param list y: List of y values.</p>
</dd></dl>

<dl class="function">
<dt id="SimulatePulses.gaus">
<code class="descclassname">SimulatePulses.</code><code class="descname">gaus</code><span class="sig-paren">(</span><em>x</em>, <em>a</em>, <em>x0</em>, <em>sigma</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/SimulatePulses.html#gaus"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#SimulatePulses.gaus" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines a gaussian function.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>x</strong> (<em>list</em>) – List of values.</li>
<li><strong>a</strong> (<em>float</em>) – Amplitude of the function.</li>
<li><strong>x0</strong> (<em>float</em>) – Expected value.</li>
<li><strong>sigma</strong> (<em>float</em>) – Sigma value.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="function">
<dt id="SimulatePulses.simulate_pulses">
<code class="descclassname">SimulatePulses.</code><code class="descname">simulate_pulses</code><span class="sig-paren">(</span><em>num_events=2, time_range=array([0.00000000e+00, 8.00320128e-10, 1.60064026e-09, ...,        1.99839936e-06, 1.99919968e-06, 2.00000000e-06]), eta_stats=[5e-08, 0], amp_stats=[0.1, 0], jitter_stats=[2e-06, 0], trigger_threshold=None, baseline=0.0, trigger_offset=None, num_pulses=None, possion_parameter=1, plotting=False, plot_pulse=False, save=True, output_dir=None</em><span class="sig-paren">)</span><a class="reference internal" href="_modules/SimulatePulses.html#simulate_pulses"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#SimulatePulses.simulate_pulses" title="Permalink to this definition">¶</a></dt>
<dd><p>Simulates Landau pulses with noise or jitter. 
Returns ScopeData object.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">SimulatePulses</span>
<span class="n">SimulatePulses</span><span class="o">.</span><span class="n">simulate_pulses</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mf">2e-06</span><span class="p">,</span> <span class="mi">2500</span><span class="p">),</span> 
                         <span class="p">[</span><span class="mf">5e-08</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span> <span class="p">,[</span><span class="mf">1e-01</span><span class="p">,</span><span class="mi">0</span><span class="p">],[</span><span class="mf">2e-06</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span> 
                         <span class="n">plotting</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">plot_pulse</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
 <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>
</div>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>num_events</strong> (<em>integer</em>) – Number of files of events to create.</li>
<li><strong>time_range</strong> (<em>array</em>) – Time range (x axis) for simulation.</li>
<li><strong>eta_stats</strong> (<em>list</em>) – List containing a mean value and a standard deviation of eta values of pulses: ([mean value, std dev]).</li>
<li><strong>jitter_stats</strong> (<em>list</em>) – List containing a mean value and a standard deviation of jitter (variance) of data: ([mean value, std dev]).</li>
<li><strong>amp_stats</strong> (<em>list</em>) – List containing lower and upper bounds of amplitude over a random distribution: ([min, max]).</li>
<li><strong>trigger_threshold</strong> (<em>bool/optional</em>) – Simulates an oscilloscope trigger threshold. The first pulse of which amplitude is equal to or greater than the trigger threshold will be found at the trigger offset. If None, it simulates a random scope window.</li>
<li><strong>baseline</strong> (<em>float/optional</em>) – Sets a baseline voltage.</li>
<li><strong>trigger_offset</strong> (<em>float/optional</em>) – X value of a triggered spot; If trigger_offset == None, the default trigger offset is 1/10 of the time range.</li>
<li><strong>num_pulses</strong> (<em>integer/optional</em>) – Number of pulses per event. If None, the number is picked randomly from poisson distribution.</li>
<li><strong>possion_parameter</strong> (<em>float/optional</em>) – Number of pulses randomly picked based on Possion Distribution.</li>
<li><strong>plotting</strong> (<em>bool/optional</em>) – If True, it plots the simulated pulse.</li>
<li><strong>plot_pulse</strong> (<em>bool/optional</em>) – If True, it plots landau pulses.</li>
<li><strong>save</strong> (<em>bool/optional</em>) – If True, it saves the pulse simulation in the output directory.</li>
<li><strong>output_dir</strong> (<em>str/optional</em>) – Directory to a folder for the saved csv files. If None, it saves the csv files in a newly created folder in working directory.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

</div>
</div>


          </div>
          
        </div>
      </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
  <h3><a href="index.html">Table Of Contents</a></h3>
  <ul>
<li><a class="reference internal" href="#">Documentation for PulsePy</a><ul>
<li><a class="reference internal" href="#introduction">Introduction</a></li>
<li><a class="reference internal" href="#requirements-txt">requirements.txt</a></li>
<li><a class="reference internal" href="#module-ScopeTrace">ScopeTrace.py</a></li>
<li><a class="reference internal" href="#module-ScopeData">ScopeData.py</a></li>
<li><a class="reference internal" href="#module-SimulatePulses">SimulatePulses.py</a></li>
<li><a class="reference internal" href="#module-SimulatePulses">SimulatePulses.py</a></li>
</ul>
</li>
</ul>
<div class="relations">
<h3>Related Topics</h3>
<ul>
  <li><a href="index.html">Documentation overview</a><ul>
      <li>Previous: <a href="index.html" title="previous chapter">Documentation for PulsePy</a></li>
      <li>Next: <a href="Install_comp.html" title="next chapter">Documentation for Installing CentOS</a></li>
  </ul></li>
</ul>
</div>
  <div role="note" aria-label="source link">
    <h3>This Page</h3>
    <ul class="this-page-menu">
      <li><a href="_sources/PulsePy.rst.txt"
            rel="nofollow">Show Source</a></li>
    </ul>
   </div>
<div id="searchbox" style="display: none" role="search">
  <h3>Quick search</h3>
    <div class="searchformwrapper">
    <form class="search" action="search.html" method="get">
      <input type="text" name="q" />
      <input type="submit" value="Go" />
      <input type="hidden" name="check_keywords" value="yes" />
      <input type="hidden" name="area" value="default" />
    </form>
    </div>
</div>
<script type="text/javascript">$('#searchbox').show(0);</script>
        </div>
      </div>
      <div class="clearer"></div>
    </div>
    <div class="footer">
      &copy;2018, Kiryeong Park, Eli Wirth-Apley.
      
      |
      Powered by <a href="http://sphinx-doc.org/">Sphinx 1.7.5</a>
      &amp; <a href="https://github.com/bitprophet/alabaster">Alabaster 0.7.11</a>
      
      |
      <a href="_sources/PulsePy.rst.txt"
          rel="nofollow">Page source</a>
    </div>

    

    
  </body>
</html>
