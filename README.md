Node Printer Prebuild
============
Native bind printers on POSIX and Windows OS from Node.js, electron and node-webkit.

> It just works with Node 12 because of @thiagoelg in his [PR](https://github.com/tojocky/node-printer/pull/261)

> Prebuild and CI integration courtesy of @ekoeryanto in his [FORK](https://github.com/ekoeryanto/node-printer)
___
### **Below is the original README**
___
### Reason:

I was involved in a project where I need to print from Node.JS. This is the reason why I created this project and I want to share my code with others.


### Features:

* no dependecies;
* native method wrappers from Windows  and POSIX (which uses [CUPS 1.4/MAC OS X 10.6](http://cups.org/)) APIs;
* compatible with node v0.8.x, 0.9.x and v0.11.x (with 0.11.9 and 0.11.13) v20.x.x;
* compatible with node-webkit v0.8.x and 0.9.2;
* `getPrinters()` to enumerate all installed printers with current jobs and statuses;
* `getPrinter(printerName)` to get a specific/default printer info with current jobs and statuses;
* `getPrinterDriverOptions(printerName)` ([POSIX](http://en.wikipedia.org/wiki/POSIX) only) to get a specific/default printer driver options such as supported paper size and other info
* `getSelectedPaperSize(printerName)` ([POSIX](http://en.wikipedia.org/wiki/POSIX) only) to get a specific/default printer default paper size from its driver options
* `getDefaultPrinterName()` return the default printer name;
* `printDirect(options)` to send a job to a specific/default printer, now supports [CUPS options](http://www.cups.org/documentation.php/options.html) passed in the form of a JS object (see `cancelJob.js` example). To print a PDF from windows it is possible by using [node-pdfium module](https://github.com/tojocky/node-pdfium) to convert a PDF format into EMF and after to send to printer as EMF;
* `printFile(options)`  ([POSIX](http://en.wikipedia.org/wiki/POSIX) only) to print a file;
* `getSupportedPrintFormats()` to get all possible print formats for printDirect method which depends on OS. `RAW` and `TEXT` are supported from all OS-es;
* `getJob(printerName, jobId)` to get a specific job info including job status;
* `setJob(printerName, jobId, command)` to send a command to a job (e.g. `'CANCEL'` to cancel the job);
* `getSupportedJobCommands()` to get supported job commands for setJob() depends on OS. `'CANCEL'` command is supported from all OS-es.


### How to install:
```
npm install consistem-node-printer
```

### How to use:

See [examples](https://github.com/consistem/node-printer/tree/main/examples)

### Author(s):

* Ion Lupascu, ionlupascu@gmail.com

### Contibutors:

* Thiago Lugli, @thiagoelg
* Eko Eryanto, @ekoeryanto
* Fylipe Amorim, @fylipeamorim

Feel free to download, test and propose new futures

### License:
 [The MIT License (MIT)](http://opensource.org/licenses/MIT)
