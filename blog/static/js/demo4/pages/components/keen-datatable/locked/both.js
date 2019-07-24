/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "../src/assets/js/theme/pages/components/keen-datatable/locked/both.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "../src/assets/js/theme/pages/components/keen-datatable/locked/both.js":
/*!*****************************************************************************!*\
  !*** ../src/assets/js/theme/pages/components/keen-datatable/locked/both.js ***!
  \*****************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
eval("\r\n// Class definition\r\n\r\nvar KTDefaultDatatableDemo = function() {\r\n    // Private functions\r\n\r\n    // basic demo\r\n    var demo = function() {\r\n\r\n        var datatable = $('.kt_datatable').KTDatatable({\r\n            data: {\r\n                type: 'remote',\r\n                source: {\r\n                    read: {\r\n                        url: 'https://keenthemes.com/keen/themes/themes/keen/dist/preview/inc/api/datatables/demos/default.php',\r\n                    },\r\n                },\r\n                pageSize: 20,\r\n                serverPaging: true,\r\n                serverFiltering: true,\r\n                serverSorting: true,\r\n            },\r\n\r\n            layout: {\r\n                theme: 'default',\r\n                class: '',\r\n                scroll: true,\r\n                height: 550,\r\n                footer: false,\r\n            },\r\n\r\n            sortable: true,\r\n\r\n            filterable: false,\r\n\r\n            pagination: true,\r\n\r\n            search: {\r\n                input: $('#generalSearch'),\r\n            },\r\n\r\n            columns: [{\r\n                field: 'employee_id',\r\n                title: 'Employee ID',\r\n                locked: {\r\n                    left: 'lg'\r\n                },\r\n            }, {\r\n                field: 'name',\r\n                title: 'Name',\r\n                locked: {\r\n                    left: 'lg'\r\n                },\r\n                template: function(row) {\r\n                    return row.first_name + ' ' + row.last_name;\r\n                },\r\n            }, {\r\n                field: 'email',\r\n                width: 150,\r\n                title: 'Email',\r\n            }, {\r\n                field: 'phone',\r\n                title: 'Phone',\r\n            }, {\r\n                field: 'hire_date',\r\n                title: 'Hire Date',\r\n                type: 'date',\r\n                format: 'MM/DD/YYYY',\r\n            }, {\r\n                field: 'gender',\r\n                title: 'Gender',\r\n            }, {\r\n                field: 'department',\r\n                title: 'Department',\r\n            }, {\r\n                field: 'address',\r\n                title: 'Address',\r\n            }, {\r\n                field: 'website',\r\n                title: 'Website',\r\n            }, {\r\n                field: 'salary',\r\n                title: 'Salary',\r\n            }, {\r\n                field: 'notes',\r\n                title: 'Notes',\r\n                width: 300,\r\n            }, {\r\n                field: 'status',\r\n                title: 'Status',\r\n                locked: {\r\n                    right: 'lg'\r\n                },\r\n                // callback function support for column rendering\r\n                template: function(row) {\r\n                    var status = {\r\n                        1: {\r\n                            'title': 'Pending',\r\n                            'class': 'kt-badge--brand'\r\n                        },\r\n                        2: {\r\n                            'title': 'Delivered',\r\n                            'class': ' kt-badge--metal'\r\n                        },\r\n                        3: {\r\n                            'title': 'Canceled',\r\n                            'class': ' kt-badge--primary'\r\n                        },\r\n                        4: {\r\n                            'title': 'Success',\r\n                            'class': ' kt-badge--success'\r\n                        },\r\n                        5: {\r\n                            'title': 'Info',\r\n                            'class': ' kt-badge--info'\r\n                        },\r\n                        6: {\r\n                            'title': 'Danger',\r\n                            'class': ' kt-badge--danger'\r\n                        },\r\n                        7: {\r\n                            'title': 'Warning',\r\n                            'class': ' kt-badge--warning'\r\n                        },\r\n                    };\r\n                    return '<span class=\"kt-badge ' + status[row.status].class + ' kt-badge--inline kt-badge--pill\">' + status[row.status].title + '</span>';\r\n                },\r\n            }, {\r\n                field: 'type',\r\n                title: 'Type',\r\n                locked: {\r\n                    right: 'lg'\r\n                },\r\n                autoHide: false,\r\n                // callback function support for column rendering\r\n                template: function(row) {\r\n                    var status = {\r\n                        1: {\r\n                            'title': 'Online',\r\n                            'state': 'danger'\r\n                        },\r\n                        2: {\r\n                            'title': 'Retail',\r\n                            'state': 'primary'\r\n                        },\r\n                        3: {\r\n                            'title': 'Direct',\r\n                            'state': 'accent'\r\n                        },\r\n                    };\r\n                    return '<span class=\"kt-badge kt-badge--' + status[row.type].state + ' kt-badge--dot\"></span>&nbsp;<span class=\"kt-font-bold kt-font-' + status[row.type].state + '\">' +\r\n                        status[row.type].title + '</span>';\r\n                },\r\n            }, {\r\n                field: 'Actions',\r\n                title: 'Actions',\r\n                sortable: false,\r\n                width: 110,\r\n                overflow: 'visible',\r\n                locked: {\r\n                    right: 'lg'\r\n                },\r\n                autoHide: false,\r\n                template: function() {\r\n                    return '\\\r\n\t\t\t\t\t\t\t<div class=\"dropdown\">\\\r\n\t\t\t\t\t\t\t\t<a href=\"javascript:;\" class=\"btn btn-sm btn-clean btn-icon btn-icon-md\" data-toggle=\"dropdown\">\\\r\n\t                                <i class=\"la la-ellipsis-h\"></i>\\\r\n\t                            </a>\\\r\n\t\t\t\t\t\t\t    <div class=\"dropdown-menu dropdown-menu-right\">\\\r\n\t\t\t\t\t\t\t        <a class=\"dropdown-item\" href=\"#\"><i class=\"la la-edit\"></i> Edit Details</a>\\\r\n\t\t\t\t\t\t\t        <a class=\"dropdown-item\" href=\"#\"><i class=\"la la-leaf\"></i> Update Status</a>\\\r\n\t\t\t\t\t\t\t        <a class=\"dropdown-item\" href=\"#\"><i class=\"la la-print\"></i> Generate Report</a>\\\r\n\t\t\t\t\t\t\t    </div>\\\r\n\t\t\t\t\t\t\t</div>\\\r\n\t\t\t\t\t\t\t<a href=\"javascript:;\" class=\"btn btn-sm btn-clean btn-icon btn-icon-md\" title=\"Edit details\">\\\r\n\t\t\t\t\t\t\t\t<i class=\"la la-edit\"></i>\\\r\n\t\t\t\t\t\t\t</a>\\\r\n\t\t\t\t\t\t\t<a href=\"javascript:;\" class=\"btn btn-sm btn-clean btn-icon btn-icon-md\" title=\"Delete\">\\\r\n\t\t\t\t\t\t\t\t<i class=\"la la-trash\"></i>\\\r\n\t\t\t\t\t\t\t</a>\\\r\n\t\t\t\t\t\t';\r\n                },\r\n            }],\r\n\r\n        });\r\n\r\n        $('#kt_form_status').on('change', function() {\r\n            datatable.search($(this).val().toLowerCase(), 'status');\r\n        });\r\n\r\n        $('#kt_form_type').on('change', function() {\r\n            datatable.search($(this).val().toLowerCase(), 'type');\r\n        });\r\n\r\n        $('#kt_form_status,#kt_form_type').selectpicker();\r\n\r\n    };\r\n\r\n    return {\r\n        // public functions\r\n        init: function() {\r\n            demo();\r\n        }\r\n    };\r\n}();\r\n\r\njQuery(document).ready(function() {\r\n    KTDefaultDatatableDemo.init();\r\n});\n\n//# sourceURL=webpack:///../src/assets/js/theme/pages/components/keen-datatable/locked/both.js?");

/***/ })

/******/ });