![AI4I Banner](https://gallery.mailchimp.com/f98d5ac0a3fbbdcdda35136ab/images/2002af76-5fd4-4185-9d49-28558b6b8772.png)
# Hands-on Machine Learning Workshop (SG HDB Resale)
The instructions listed below are for you to get started on interacting with the resources contained in this repository, particularly the Jupyter Notebooks, for the purpose of AI4I's `Hands-on Machine Learning Workshop (SG HDB Resale)`.

# Logistics
__For on-site sessions:__ Participants of this workshop are required to **bring their own laptops**. No local installation of softwares are required other than **web browsers**. We recommend either Chrome or Firefox for browsers. **WiFi connection will be provided**, however please ensure that your laptop can connect to public SSIDs. Staff laptops or laptops with SOEs have a likelihood of not being able to connect to our WiFi connection. It is recommended that you use your personal laptop.

# Instructions/Guide
Follow the instructions below to set up the environment needed for the workshop:
1. Head over to [mybinder](https://mybinder.org/).
2. Paste this repository's link (`https://github.com/kelaberetiv/ai4i-sg-hdb-resale-abr`) to the field '`GitHub repository name or URL`'.
3. Click on the button '`launch`' and wait for a couple of minutes.
4. Once successful, you would be presented with the following interface:
![mybinder Interface](https://i.imgur.com/rpgRmSP.png)
5. Feel free to navigate through each of the folders and files.


Optional:
+ To view created SQLite databases through a GUI during the session, you can download [SQLite Browser](https://sqlitebrowser.org/dl/) on your local machine.

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
