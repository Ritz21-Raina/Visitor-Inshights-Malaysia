# Overview
This project visualizes foreign arrivals in Malaysia from 2020 to 2024, exploring demographic and geographical patterns across states, genders, nationalities, and modes of entry. The dashboard aims to highlight travel trends and regional travel dynamics through a clear, interactive design built using Tableau and the Munaver visualization framework.


# Tableau Visualisation Link :
https://public.tableau.com/views/DataVisualisation1_17567053236730/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link


# Munaver Visualisation Framework
### Domain:
My visualization focuses on foreign arrivals in Malaysia from 2020 to 2024, analyzing key attributes such as year, month, gender, nationality, and state of arrival.
An additional dataset on points of entry (air, water, and land) was integrated to provide a more complete view of how travelers enter different Malaysian states.

### Why:
- To observe changes in foreign arrivals over five years.
- To identify the most visited Malaysian states.
- To determine which nationalities visit Malaysia the most.
- To analyze gender-based travel trends.
- To explore modes of entry (air, land, water) for top states.
- To uncover seasonal travel patterns across months and years.

### What:
Foreign Arrivals Dataset: [data.gov.my – Arrivals by State of Entry](https://data.gov.my/data-catalogue/arrivals_soe)
Point of Entry Dataset: [Kaggle – Malaysia Foreign Arrivals](https://www.kaggle.com/code/yyxian/malaysia-foreign-arrivals?select=poe.csv) 
The datasets were cleaned and merged using Python (Pandas). The number of entry points by type (air, land, water) was first aggregated and then combined with the main arrivals dataset for enhanced insights.

### How:
1. Line Chart: Shows the overall trend of arrivals, highlighting annual fluctuations and recovery patterns.
2. Pie Chart (Gender Distribution): Compares male and female arrivals per year for clear gender insight.
3. Lollipop Chart (Top 10 Nationalities): Visually compares arrival volumes, supported by mini geographic maps.
4. Stacked Bar Chart (Modes of Transport): Displays the proportion of air, land, and sea entries by state.
5. Horizontal Bar Chart: Compares arrival counts across all Malaysian states.
6.Heatmap (Seasonal Trends): Reveals monthly arrival intensity using a color gradient for clear visual contrast.

