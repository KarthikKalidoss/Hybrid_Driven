<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>Test Report</title>
    <link href="assets/style.css" rel="stylesheet" type="text/css"/></head>
  <body onLoad="init()">
    <script>/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this file,
 * You can obtain one at http://mozilla.org/MPL/2.0/. */


function toArray(iter) {
    if (iter === null) {
        return null;
    }
    return Array.prototype.slice.call(iter);
}

function find(selector, elem) {
    if (!elem) {
        elem = document;
    }
    return elem.querySelector(selector);
}

function find_all(selector, elem) {
    if (!elem) {
        elem = document;
    }
    return toArray(elem.querySelectorAll(selector));
}

function sort_column(elem) {
    toggle_sort_states(elem);
    var colIndex = toArray(elem.parentNode.childNodes).indexOf(elem);
    var key;
    if (elem.classList.contains('numeric')) {
        key = key_num;
    } else if (elem.classList.contains('result')) {
        key = key_result;
    } else {
        key = key_alpha;
    }
    sort_table(elem, key(colIndex));
}

function show_all_extras() {
    find_all('.col-result').forEach(show_extras);
}

function hide_all_extras() {
    find_all('.col-result').forEach(hide_extras);
}

function show_extras(colresult_elem) {
    var extras = colresult_elem.parentNode.nextElementSibling;
    var expandcollapse = colresult_elem.firstElementChild;
    extras.classList.remove("collapsed");
    expandcollapse.classList.remove("expander");
    expandcollapse.classList.add("collapser");
}

function hide_extras(colresult_elem) {
    var extras = colresult_elem.parentNode.nextElementSibling;
    var expandcollapse = colresult_elem.firstElementChild;
    extras.classList.add("collapsed");
    expandcollapse.classList.remove("collapser");
    expandcollapse.classList.add("expander");
}

function show_filters() {
    var filter_items = document.getElementsByClassName('filter');
    for (var i = 0; i < filter_items.length; i++)
        filter_items[i].hidden = false;
}

function add_collapse() {
    // Add links for show/hide all
    var resulttable = find('table#results-table');
    var showhideall = document.createElement("p");
    showhideall.innerHTML = '<a href="javascript:show_all_extras()">Show all details</a> / ' +
                            '<a href="javascript:hide_all_extras()">Hide all details</a>';
    resulttable.parentElement.insertBefore(showhideall, resulttable);

    // Add show/hide link to each result
    find_all('.col-result').forEach(function(elem) {
        var collapsed = get_query_parameter('collapsed') || 'Passed';
        var extras = elem.parentNode.nextElementSibling;
        var expandcollapse = document.createElement("span");
        if (extras.classList.contains("collapsed")) {
            expandcollapse.classList.add("expander")
        } else if (collapsed.includes(elem.innerHTML)) {
            extras.classList.add("collapsed");
            expandcollapse.classList.add("expander");
        } else {
            expandcollapse.classList.add("collapser");
        }
        elem.appendChild(expandcollapse);

        elem.addEventListener("click", function(event) {
            if (event.currentTarget.parentNode.nextElementSibling.classList.contains("collapsed")) {
                show_extras(event.currentTarget);
            } else {
                hide_extras(event.currentTarget);
            }
        });
    })
}

function get_query_parameter(name) {
    var match = RegExp('[?&]' + name + '=([^&]*)').exec(window.location.search);
    return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
}

function init () {
    reset_sort_headers();

    add_collapse();

    show_filters();

    sort_column(find('.initial-sort'));

    find_all('.sortable').forEach(function(elem) {
        elem.addEventListener("click",
                              function(event) {
                                  sort_column(elem);
                              }, false)
    });

};

function sort_table(clicked, key_func) {
    var rows = find_all('.results-table-row');
    var reversed = !clicked.classList.contains('asc');
    var sorted_rows = sort(rows, key_func, reversed);
    /* Whole table is removed here because browsers acts much slower
     * when appending existing elements.
     */
    var thead = document.getElementById("results-table-head");
    document.getElementById('results-table').remove();
    var parent = document.createElement("table");
    parent.id = "results-table";
    parent.appendChild(thead);
    sorted_rows.forEach(function(elem) {
        parent.appendChild(elem);
    });
    document.getElementsByTagName("BODY")[0].appendChild(parent);
}

function sort(items, key_func, reversed) {
    var sort_array = items.map(function(item, i) {
        return [key_func(item), i];
    });

    sort_array.sort(function(a, b) {
        var key_a = a[0];
        var key_b = b[0];

        if (key_a == key_b) return 0;

        if (reversed) {
            return (key_a < key_b ? 1 : -1);
        } else {
            return (key_a > key_b ? 1 : -1);
        }
    });

    return sort_array.map(function(item) {
        var index = item[1];
        return items[index];
    });
}

function key_alpha(col_index) {
    return function(elem) {
        return elem.childNodes[1].childNodes[col_index].firstChild.data.toLowerCase();
    };
}

function key_num(col_index) {
    return function(elem) {
        return parseFloat(elem.childNodes[1].childNodes[col_index].firstChild.data);
    };
}

function key_result(col_index) {
    return function(elem) {
        var strings = ['Error', 'Failed', 'Rerun', 'XFailed', 'XPassed',
                       'Skipped', 'Passed'];
        return strings.indexOf(elem.childNodes[1].childNodes[col_index].firstChild.data);
    };
}

function reset_sort_headers() {
    find_all('.sort-icon').forEach(function(elem) {
        elem.parentNode.removeChild(elem);
    });
    find_all('.sortable').forEach(function(elem) {
        var icon = document.createElement("div");
        icon.className = "sort-icon";
        icon.textContent = "vvv";
        elem.insertBefore(icon, elem.firstChild);
        elem.classList.remove("desc", "active");
        elem.classList.add("asc", "inactive");
    });
}

function toggle_sort_states(elem) {
    //if active, toggle between asc and desc
    if (elem.classList.contains('active')) {
        elem.classList.toggle('asc');
        elem.classList.toggle('desc');
    }

    //if inactive, reset all other functions and add ascending active
    if (elem.classList.contains('inactive')) {
        reset_sort_headers();
        elem.classList.remove('inactive');
        elem.classList.add('active');
    }
}

function is_all_rows_hidden(value) {
  return value.hidden == false;
}

function filter_table(elem) {
    var outcome_att = "data-test-result";
    var outcome = elem.getAttribute(outcome_att);
    class_outcome = outcome + " results-table-row";
    var outcome_rows = document.getElementsByClassName(class_outcome);

    for(var i = 0; i < outcome_rows.length; i++){
        outcome_rows[i].hidden = !elem.checked;
    }

    var rows = find_all('.results-table-row').filter(is_all_rows_hidden);
    var all_rows_hidden = rows.length == 0 ? true : false;
    var not_found_message = document.getElementById("not-found-message");
    not_found_message.hidden = !all_rows_hidden;
}
</script>
    <h1>test_login.py</h1>
    <p>Report generated on 23-Nov-2020 at 13:12:29 by <a href="https://pypi.python.org/pypi/pytest-html">pytest-html</a> v2.1.1</p>
    <h2>Environment</h2>
    <table id="environment">
      <tr>
        <td>Module Name</td>
        <td>SQA CAF ADMIN PORTAL</td></tr>
      <tr>
        <td>Packages</td>
        <td>{"pluggy": "0.13.1", "py": "1.9.0", "pytest": "6.1.2"}</td></tr>
      <tr>
        <td>Platform</td>
        <td>Windows-10-10.0.17763-SP0</td></tr>
      <tr>
        <td>Project Name</td>
        <td>SQA SUPPORT AUTOMATION</td></tr>
      <tr>
        <td>Python</td>
        <td>3.7.2</td></tr>
      <tr>
        <td>Tester</td>
        <td>KARTHIK KALIDOSS</td></tr></table>
    <h2>Summary</h2>
    <p>7 tests ran in 46.68 seconds. </p>
    <p class="filter" hidden="true">(Un)check the boxes to filter the results.</p><input checked="true" class="filter" data-test-result="passed" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="passed">6 passed</span>, <input checked="true" class="filter" data-test-result="skipped" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="skipped">1 skipped</span>, <input checked="true" class="filter" data-test-result="failed" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="failed">1 failed</span>, <input checked="true" class="filter" data-test-result="error" disabled="true" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="error">0 errors</span>, <input checked="true" class="filter" data-test-result="xfailed" disabled="true" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="xfailed">0 expected failures</span>, <input checked="true" class="filter" data-test-result="xpassed" disabled="true" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="xpassed">0 unexpected passes</span>
    <h2>Results</h2>
    <table id="results-table">
      <thead id="results-table-head">
        <tr>
          <th class="sortable result initial-sort" col="result">Result</th>
          <th class="sortable" col="name">Test</th>
          <th class="sortable numeric" col="duration">Duration</th>
          <th>Links</th></tr>
        <tr hidden="true" id="not-found-message">
          <th colspan="4">No results found. Try to check the filters</th></tr></thead>
      <tbody class="failed results-table-row">
        <tr>
          <td class="col-result">Failed</td>
          <td class="col-name">Test_Cases/test_login_allure.py::Test_001_login::test_Home_Page_Title</td>
          <td class="col-duration">1.69</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log">self = &lt;Test_Cases.test_login_allure.Test_001_login object at 0x00000271A02CF470&gt;<br/>driver_setup = &lt;selenium.webdriver.chrome.webdriver.WebDriver (session=&quot;7f0e7cc5a14a30b2ad30d56e386e1c82&quot;)&gt;<br/><br/>    def test_Home_Page_Title(self, driver_setup):<br/>        self.logger.info(&#x27;*************** TEST_001_LOGIN *******************&#x27;)<br/>        self.logger.info(&#x27;*************** VERIFYING URL / HOME PAGE TITLE *******************&#x27;)<br/>        self.driver = driver_setup<br/>        self.driver.get(self.url)<br/>        actual_title = self.driver.title<br/>        if actual_title == &quot;Log in | SQA Internal Portal1&quot;:<br/>            assert True<br/>            self.driver.close()<br/>            self.logger.info(&#x27;*************** URL WORKING FINE AND HOME PAGE TITLE IS PASSED *******************&#x27;)<br/>    <br/>        else:<br/>            allure.attach(self.driver.get_screenshot_as_png(), name=&#x27;Test_URL&#x27;, attachment_type=AttachmentType.PNG)<br/>            self.driver.save_screenshot(&quot;.\\Screenshots\\&quot; + &quot; Test_Home_Page_Title.png&quot;)<br/>            self.driver.close()<br/>            self.logger.error(&#x27;*************** URL AND HOME PAGE TITLE IS FAILED *******************&#x27;)<br/>&gt;           assert False<br/><span class="error">E           assert False</span><br/><br/>Test_Cases\test_login_allure.py:38: AssertionError<br/> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_login_allure.py:23 *************** TEST_001_LOGIN *******************
[32mINFO    [0m root:test_login_allure.py:24 *************** VERIFYING URL / HOME PAGE TITLE *******************
[31m[1mERROR   [0m root:test_login_allure.py:37 *************** URL AND HOME PAGE TITLE IS FAILED *******************<br/></div></td></tr></tbody>
      <tbody class="skipped results-table-row">
        <tr>
          <td class="col-result">Skipped</td>
          <td class="col-name">Test_Cases/test_login_allure.py::Test_001_login::test_skip</td>
          <td class="col-duration">0.00</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log">(&#x27;C:\\Karthik\\New_Projects\\Hybrid_Driven\\Test_Cases\\test_login_allure.py&#x27;, 42, &#x27;Skipped: SKIPPING THE TEST, DO IT LATER.......&#x27;)<br/></div></td></tr></tbody>
      <tbody class="passed results-table-row">
        <tr>
          <td class="col-result">Passed</td>
          <td class="col-name">Test_Cases/test_button_validations.py::Test_003_button_validation::test_buttons_validation</td>
          <td class="col-duration">2.88</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log"> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_button_validations.py:17 ***********************Test_003_BUTTON-VALIDATIONS************************** 
[32mINFO    [0m root:test_button_validations.py:18 *************** VERIFYING CAF ADMIN PORTAL VALIDATION *******************
[32mINFO    [0m root:test_button_validations.py:28 *************** CAF ADMIN PORTAL VALIDATION LOGIN TEST IS PASSED *******************
[32mINFO    [0m root:test_button_validations.py:43 ********* EXCEPTIONAL ENTRIES BUTTON VALIDATION IS PASSED ****************
[32mINFO    [0m root:test_button_validations.py:56 ********* CLC BUTTON VALIDATION IS PASSED ****************
[32mINFO    [0m root:test_button_validations.py:69 ********* CERTIFICATE DATE BUTTON VALIDATION TEST IS  PASSED ****************
[32mINFO    [0m root:test_button_validations.py:82 ********* CERTIFICATE RE-PRINT BUTTON VALIDATION TEST IS PASSED ****************
[32mINFO    [0m root:test_button_validations.py:95 **** ASSESSMENT ARRANGEMENTS VALID  VALUES BUTTON VALIDATION TEST IS PASSED *****
[32mINFO    [0m root:test_button_validations.py:123 ********* USER NAME PROFILE BUTTON IS NOT ENABLED - PASSED ****************
[32mINFO    [0m root:test_button_validations.py:134 *****************END OF BUTTON VALIDATION TEST*****************
[32mINFO    [0m root:test_button_validations.py:135 ****************END OF Test_003_BUTTONS VALIDATIONS*****************<br/></div></td></tr></tbody>
      <tbody class="passed results-table-row">
        <tr>
          <td class="col-result">Passed</td>
          <td class="col-name">Test_Cases/test_exceptional_entries.py::Test_004_login::test_login</td>
          <td class="col-duration">2.30</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log"> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_exceptional_entries.py:20 *************** VERIFYING CAF ADMIN PORTAL VALIDATION *******************
[32mINFO    [0m root:test_exceptional_entries.py:30 *************** CAF ADMIN PORTAL VALIDATION LOGIN TEST IS PASSED *******************<br/></div></td></tr></tbody>
      <tbody class="passed results-table-row">
        <tr>
          <td class="col-result">Passed</td>
          <td class="col-name">Test_Cases/test_login.py::Test_001_login::test_Home_Page_Title</td>
          <td class="col-duration">0.95</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log"> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_login.py:21 *************** TEST_001_LOGIN *******************
[32mINFO    [0m root:test_login.py:22 *************** VERIFYING URL / HOME PAGE TITLE *******************
[32mINFO    [0m root:test_login.py:29 *************** URL WORKING FINE AND HOME PAGE TITLE IS PASSED *******************<br/></div></td></tr></tbody>
      <tbody class="passed results-table-row">
        <tr>
          <td class="col-result">Passed</td>
          <td class="col-name">Test_Cases/test_login.py::Test_001_login::test_login</td>
          <td class="col-duration">2.79</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log"> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_login.py:40 *************** VERIFYING CAF ADMIN PORTAL VALIDATION *******************
[32mINFO    [0m root:test_login.py:50 *************** CAF ADMIN PORTAL VALIDATION LOGIN TEST IS PASSED *******************
[32mINFO    [0m root:test_login.py:62 *****************END OF URL AND LOGIN VALIDATION TEST*****************
[32mINFO    [0m root:test_login.py:63 *********************END OF Test_001_LOGIN*****************<br/></div></td></tr></tbody>
      <tbody class="passed results-table-row">
        <tr>
          <td class="col-result">Passed</td>
          <td class="col-name">Test_Cases/test_login_allure.py::Test_001_login::test_login</td>
          <td class="col-duration">2.58</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log"> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_login_allure.py:46 *************** VERIFYING CAF ADMIN PORTAL VALIDATION *******************
[32mINFO    [0m root:test_login_allure.py:56 *************** CAF ADMIN PORTAL VALIDATION LOGIN TEST IS PASSED *******************
[32mINFO    [0m root:test_login_allure.py:68 *****************END OF URL AND LOGIN VALIDATION TEST*****************
[32mINFO    [0m root:test_login_allure.py:69 *******************END OF Test_001_login*****************<br/></div></td></tr></tbody>
      <tbody class="passed results-table-row">
        <tr>
          <td class="col-result">Passed</td>
          <td class="col-name">Test_Cases/test_login_ddt.py::Test_002_DDT_login::test_login_ddt</td>
          <td class="col-duration">5.51</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log"> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_login_ddt.py:21 ***********************Test_002_DDT_LOGIN************************** 
[32mINFO    [0m root:test_login_ddt.py:22 VERIFYING CAF ADMIN LOGIN VALIDATION - DATA DRIVEN TEST
[32mINFO    [0m root:test_login_ddt.py:46 *************** CAF ADMIN LOGIN VALIDATION TEST IS PASSED *******************
[32mINFO    [0m root:test_login_ddt.py:64 *************** CAF ADMIN LOGIN VALIDATION TEST IS PASSED *******************
[32mINFO    [0m root:test_login_ddt.py:64 *************** CAF ADMIN LOGIN VALIDATION TEST IS PASSED *******************
[32mINFO    [0m root:test_login_ddt.py:64 *************** CAF ADMIN LOGIN VALIDATION TEST IS PASSED *******************
[32mINFO    [0m root:test_login_ddt.py:64 *************** CAF ADMIN LOGIN VALIDATION TEST IS PASSED *******************
[32mINFO    [0m root:test_login_ddt.py:69 CAF ADMIN LOGIN VALIDATION - DATA DRIVEN TEST IS PASSED
[32mINFO    [0m root:test_login_ddt.py:77 *****************END OF DATA DRIVEN TEST*****************
[32mINFO    [0m root:test_login_ddt.py:78 ****************END OF Test_002_DDT_LOGIN*****************<br/></div></td></tr></tbody></table></body></html>