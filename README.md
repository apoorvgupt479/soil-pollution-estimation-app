Soil Pollution Estimation App
========================================

**Relevant Sustainable Development Goals (SDG):**

*   **GOAL 3:** Good Health and Well-being
    
*   **GOAL 11:** Sustainable Cities and Communities
    
*   **GOAL 15:** Life on Land
    

Introduction
------------

Soil pollution is an often overlooked, yet highly impactful issue affecting ecosystems and human health. Urbanization and industrial activities have led to elevated levels of hazardous contaminants such as lead, cadmium, arsenic, and pesticides in the soil. These pollutants degrade soil quality, impacting agricultural productivity and introducing toxins into food chains. Despite the high stakes, there remains a lack of systematic testing and public awareness about soil contamination. This gap poses serious health risks, as exposure to toxic soils can contribute to illnesses, respiratory issues, and developmental problems in children.

The "Soil Pollution Estimation App" project addresses this critical need by providing a user-friendly platform that estimates soil contamination levels based on proximity to pollution hotspots. This tool enables users to quickly access data about their environment, fostering informed community decision-making. By promoting awareness and empowering users to understand soil health risks, this app supports efforts toward healthier, sustainable living in urban areas

Literature Review
-----------------

Soil pollution assessment methods increasingly leverage Geographic Information Systems (GIS) and spatial data analysis, with remote sensing as a notable example. This approach enables efficient monitoring of soil properties impacted by human activities, such as industrial or urban waste. For example, tools like the SQAPP mobile application provide a broader regional view of soil health threats (e.g., erosion, nutrient depletion, contamination) by offering accessible soil quality data for any selected location on a global map. Moreover, studies emphasize the importance of proximity data to estimate contamination by correlating distances to industrial hotspots and assessing heavy metal content in nearby soils. These techniques lay the groundwork for our app’s contamination estimation model, which is based on proximity and spatial data analysis.

Indian government has a soil health card scheme where the soil health is tested and their mineral content information is given to farmers. We want to raise awareness so that pollutants can also be tested for the same. 

Indian Regions Soil Image Database (IRSID) is a dataset for classification of Indian soils published by R Murugan from NIT Silchar provides the dataset for the soil types.

 NICES has carried out soil mapping for sub-regional planning under Integrated Mission for Sustainable Developed (IMSD) and other regional soil mapping projects using multi-temporal satellite data acquired from LISS-II sensors aboard IRS-1A / 1B/ 1C. Soil maps generated at 1:250,000 and 1:50,000 scales under various projects at NRSC carried out during 1985-2005 using visual interpretation of multi-temporal satellite data supported with soil profile studies and soil chemical analytical data were used.

For providing soil carbon densities, spatial outputs generated under National soil carbon pools of India - ISRO-Geosphere Biosphere project are used.

Many research papers talk about the soil pollution condition about a specific area but none have done estimation in large scale.

Materials and Methods
---------------------

1.  Data Collection:
    
    *   Contaminated cities were identified and categorized by pollutant types (e.g., lead, cadmium) based on historical data.
        
    *   Location and demographic data are loaded from a cities.csv file, which includes coordinates for each city.
        
2.  Proximity-Based Estimation Algorithm
    
    *   The Haversine formula calculates distances between cities using latitude and longitudes of the citiesto assess contamination levels according to proximity. This approach draws on studies that successfully use geostatistics and remote sensing to predict pollution levels based on distance from contamination sources.
        
    *   Contamination levels are estimated as high, medium, or low depending on the proximity to hotspots, such as regions with high lead or cadmium use.
        
    *   The contamination values for a district are assigned from a range specific to the contaminant and the proximity to the contamination hotspots.
        
    *   All the values of pollution for all districts are estimated at once and stored as pollution-estimation.csv .
        
3.  User Interface:
    
    *   The user interface, created with Tkinter
        
    *   The app allows users to select a city and view estimated contaminant levels, and other physical data for that city.
        
    *   This interface is purposely kept simple to make environmental data easily accessible to the technologically non-specialist users, similar to user-focused environmental monitoring apps like SQAPP.
        

Results and Discussion
----------------------

Our soil contamination estimates affirm the effectiveness of using proximity to hotspots as a reliable method for gauging pollution risk. Industrial and urban centers, identified as areas with significant contamination, displayed higher levels of pollutants, particularly heavy metals like lead, cadmium, and chromium, as well as pesticides and waste products. These results align with global data indicating that pollution tends to concentrate near high-activity industrial and densely populated urban areas, leading to soil degradation and elevated health risks.

If we were to map the districts on the map of India, we would see smooth trends, with higher concentrations at the hotspots and gradually decreasing levels in non-hotspot areas, similar to real-life pollution dispersion patterns. Remote sensing tools and spatial data analysis show similar trends on a regional or global scale, where proximity to pollution sources corresponds to higher contamination levels. This consistency across different methods and datasets strengthens the reliability of proximity-based assessments, making them a valuable approach when high-resolution, on-site testing is unavailable.

Our analysis also highlights the role of mapping technologies in making pollution data accessible to communities, which can use this information to guide preventive and restorative efforts. Such data-driven insights are crucial for environmental planning, helping prioritize soil health interventions in highly affected areas and raising awareness about soil contamination risks.

Conclusion
----------

Our soil contamination prediction app uses distance from pollution affected areas to give a rough estimate of the soil quality in the area. The need for this arose as there were no reliable datasets available on the internet which covered the entirety of India.

Post calculation, we made a simple application where a user can input his district and his physical data like latitude, longitude, area and population along with the soil pollution estimates like the presence of heavy metals, plastics, urban wastes, excess pesticides, e-wastes, nuclear wastes, etc. in one go.

Contribution to Sustainable Development Goals
---------------------------------------------

The Soil Pollution Estimation App aligns with:

*   Goal 3: Promotes health by offering users critical data on soil quality.
    
*   Goal 11: Supports sustainable urban planning and pollution control.
    
*   Goal 15: Encourages soil health awareness, contributing to better life on land.
    

References
----------

*   SQAPP and regional soil quality analysis tool (ISRIC).([https://www.isric.org/news/sqapp-launch](https://www.isric.org/news/sqapp-launch))
    
*   Geospatial analysis in soil contamination monitoring (MDPI Remote Sensing Special Issue).
    
*   Names and locations of various Indian districts ([https://github.com/recurze/IndianCities/blob/master/final\_districts.csv](https://github.com/recurze/IndianCities/blob/master/final_districts.csv))
    
*   Soil health card scheme ([https://soilhealth.dac.gov.in/](https://soilhealth.dac.gov.in/))
    
*   Soil Order and Group datasets  on bhuvan portal([https://www.data.gov.in/datasets\_webservices/datasets/6750984](https://www.data.gov.in/datasets_webservices/datasets/6750984))
    
*   Soil types dataset on kaggle ([https://www.kaggle.com/datasets/prasanshasatpathy/soil-types#](https://www.kaggle.com/datasets/prasanshasatpathy/soil-types#))
    
*   National Information System for Climate and Environment Studies study on soil health ([https://nices.nrsc.gov.in/products/terrestrial.php](https://nices.nrsc.gov.in/products/terrestrial.php))
    
*   Pollution Hotspots
    
    *   Chromium contamination
        
        *   [https://india.mongabay.com/2024/08/kanpurs-leather-legacy-navigating-sustainability-against-industrial-challenges](https://india.mongabay.com/2024/08/kanpurs-leather-legacy-navigating-sustainability-against-industrial-challenges/#:~:text=A paper published in 2019,River at Kanpur, which contains)
            
        *   [https://www.worstpolluted.org/projects\_reports/display/36](https://www.worstpolluted.org/projects_reports/display/36#:~:text=Sukinda Valley, in the State,ore mines in the world)
            
        *   [https://www.researchgate.net/publication/304935767\_A\_review\_on\_tannery\_pollution\_in\_Vellore\_District\_Tamil\_Nadu\_India](https://www.researchgate.net/publication/304935767_A_review_on_tannery_pollution_in_Vellore_District_Tamil_Nadu_India)
            
    *   Arsenic contamination
        
        *   [https://pmc.ncbi.nlm.nih.gov/articles/PMC2940197](https://pmc.ncbi.nlm.nih.gov/articles/PMC2940197)
            
        *   [https://pubmed.ncbi.nlm.nih.gov/16440510/](https://pubmed.ncbi.nlm.nih.gov/16440510/)
            
        *   [https://pmc.ncbi.nlm.nih.gov/articles/PMC5858255/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5858255/)
            
        *   [https://www.researchgate.net/publication/359068699\_Predicting\_the\_Distribution\_of\_Arsenic\_in\_Groundwater\_by\_a\_Geospatial\_Machine\_Learning\_Technique\_in\_the\_Two\_Most\_Affected\_Districts\_of\_Assam\_India\_The\_Public\_Health\_Implications](https://www.researchgate.net/publication/359068699_Predicting_the_Distribution_of_Arsenic_in_Groundwater_by_a_Geospatial_Machine_Learning_Technique_in_the_Two_Most_Affected_Districts_of_Assam_India_The_Public_Health_Implications)
            
    *   Mercury
        
        *   [https://www.deccanherald.com/india/bhopal-gas-tragedy-new-govt-study-shows-high-groundwater-contamination-in-some-areas-2938187](https://www.deccanherald.com/india/bhopal-gas-tragedy-new-govt-study-shows-high-groundwater-contamination-in-some-areas-2938187)
            
        *   [https://housing.com/news/companies-in-durgapur/](https://housing.com/news/companies-in-durgapur/)
            
        *   [https://www.power-technology.com/data-insights/power-plant-profile-singrauli-super-thermal-power-station-india](https://www.power-technology.com/data-insights/power-plant-profile-singrauli-super-thermal-power-station-india)
            
    *   Urban Waste
        
        *   [https://www.researchgate.net/publication/298710466\_Urbanisation\_and\_Consistency\_Measurement\_A\_Study\_on\_District\_of\_North\_24\_Parganas\_West\_Bengal\_India](https://www.researchgate.net/publication/298710466_Urbanisation_and_Consistency_Measurement_A_Study_on_District_of_North_24_Parganas_West_Bengal_India)
            
        *   [https://byjus.com/question-answer/arrange-the-following-in-decreasing-order-of-population-density-1-mysuru-2-dharwad-3-bengaluru-1/](https://byjus.com/question-answer/arrange-the-following-in-decreasing-order-of-population-density-1-mysuru-2-dharwad-3-bengaluru-1/)
            
        *   [https://ernakulam.nic.in/en/](https://ernakulam.nic.in/en/)
            
        *   [https://en.wikipedia.org/wiki/Kanpur\_Nagar\_district](https://en.wikipedia.org/wiki/Kanpur_Nagar_district)
            
        *   [https://howrah.gov.in/](https://howrah.gov.in/)
            
        *   [https://www.britannica.com/place/Ghaziabad-India](https://www.britannica.com/place/Ghaziabad-India)
            
        *   [https://hyderabad.telangana.gov.in/about-district/](https://hyderabad.telangana.gov.in/about-district/)
            
    *   Excessive Pesticides
        
        *   [https://www.britannica.com/place/Sangrur](https://www.britannica.com/place/Sangrur)
            
        *   [https://en.wikipedia.org/wiki/Thanjavur](https://en.wikipedia.org/wiki/Thanjavur)
            
        *   [https://meerutgdp.com/current-sectoral-status-of-economy-of-meerut/agriculture-sector](https://meerutgdp.com/current-sectoral-status-of-economy-of-meerut/agriculture-sector)
            
        *   [https://www.britannica.com/place/Buldhana](https://www.britannica.com/place/Buldhana)
            
        *   [https://www.cms.org.in/insights/kurnool-groundnut-venture-story-of-successful-groundnut-sales-by-kurnool-farmer-producer-company](https://www.cms.org.in/insights/kurnool-groundnut-venture-story-of-successful-groundnut-sales-by-kurnool-farmer-producer-company)
            
    *   E-waste
        
        *   [https://environment.delhi.gov.in/environment/e-waste](https://environment.delhi.gov.in/environment/e-waste)
            
        *   [https://www.greenit.co.in/e-waste-recycling-services-gurgaon.html](https://www.greenit.co.in/e-waste-recycling-services-gurgaon.html)
            
        *   [https://thescalers.com/bangalore/](https://thescalers.com/bangalore/)
            
    *   Nuclear Waste
        
        *   [https://timesofindia.indiatimes.com/city/chennai/buried-deep-a-clear-plan-for-nuclear-waste-disposal/articleshow/90216346.cms](https://timesofindia.indiatimes.com/city/chennai/buried-deep-a-clear-plan-for-nuclear-waste-disposal/articleshow/90216346.cms)
