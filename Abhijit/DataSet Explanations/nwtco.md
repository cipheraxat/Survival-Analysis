## Data from the National Wilm's Tumor Study

This is one of the comparative survival prediction dataset based on the **Histology** outcomes of some **Tumor**, which contains the predictions by a local institution and
by a central lab. There is a conclusion included too, i.e the prediction with the central lab is stronger than the local institution.

Let's have a look at the columns of the dataset.

![](https://github.com/Abhijit2505/Survival-Analysis/blob/master/Abhijit/DataSet%20Explanations/Capture%20nwtco.PNG)

* ```seqno``` - id number, may be the patient id for identification or the Histology test id to distinguish one test from the other
* ```instit``` - Histology from local institution - Consists of integer 1 and 2, which predicts the organ behavious where the tumor has occured
* ```histol``` - Histology from central lab - Consists of integer 1 and 2
* ```stage``` - Disease stage, there are 4 integers 1 to 4, each representing the stage of the Tumor
* ```study``` - Number of histology studies performed, integer
* ```rel``` - Consists of 0 and 1, may be the event indicator for survival/relapse
* ```edrel``` - Time to relapse, integer, number of days, the duration variable for the survival dataset
* ```age``` - Age in months, integer
* ```in.subcohort``` - Boolean, if included in some clinical papaer or not
