![AI4I Banner](https://gallery.mailchimp.com/f98d5ac0a3fbbdcdda35136ab/images/2002af76-5fd4-4185-9d49-28558b6b8772.png)
# Hands-on Machine Learning Workshop (SG HDB Resale)
This repository contains resources for AI for Industry's Hands-on Machine Learning Workshop (SG HDB Resale)

This repository contains instructions for you to get started on interacting with the resources, particularly the Jupyter Notebooks, for the purpose of this `Hands-on Machine Learning Workshop (SG HDB Resale)`.

# Logistics
Participants of this workshop are required to **bring their own laptops**. No local installation of softwares are required other than **web browsers**. We recommend either Chrome or Firefox for browsers. **WiFi connection will be provided**, however please ensure that your laptop can connect to public SSIDs. Staff laptops or laptops with SOEs have a likelihood of not being able to connect to our WiFi connection. It is recommended that you use your personal laptop.

# Instructions/Guide
Follow the following instructions prior to the workshop so that you can get started.

1. Make an account and log in to [Azure Notebook](https://notebooks.azure.com/) using your Microsoft account. (Create one if you have yet to do so.)
2. Navigate to `My Projects` through the selection bar at the top.
3. Click on `Upload Github Repo`, and under the field `Git repo`, enter the following: `kelaberetiv/ai4i-sg-hdb-resale-abr`
4. Click `Import` and wait for a couple of minutes for the resources to be imported.
5. Once it is done, you are all set! Feel free to navigate through each of the folders and files prior to the workshop.

Optional:
+ To view created SQLite databases through a GUI during the session, you can download [SQLite Browser](https://sqlitebrowser.org/dl/) on your local machine.

**(Visual) Instructional Video:**
https://youtu.be/ABsQmSYqGvI

# Repository Structure/File Information
```
├── README.md          <- The file that presents you with this document that you're reading right now.
├── reference          <- This folder contains resources that you can rely on should you get stuck at some point.
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling will be exported to this place.
│   └── raw            <- The original, immutable data dump. Data are obtainable through data.gov.sg
│
├── notebooks          <- Contains Jupyter Notebooks.
│
└── models             <- Trained and serialised models will be stored here.
```
