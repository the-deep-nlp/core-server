ROUNDOFF_DIGITS = 3

CATEGORIES = [
    "sectors",
    "pillars_1d",
    "pillars_2d",
    "subpillars_1d",
    "subpillars_2d",
    "age",
    "displaced",
    "gender",
    "non_displaced",
    "severity",
    "specific_needs_groups",
    "affected",
]

SECTORS_LST = [
    "first_level_tags->sectors->Agriculture",
    "first_level_tags->sectors->Cross",
    "first_level_tags->sectors->Education",
    "first_level_tags->sectors->Food security",
    "first_level_tags->sectors->Health",
    "first_level_tags->sectors->Livelihoods",
    "first_level_tags->sectors->Logistics",
    "first_level_tags->sectors->Nutrition",
    "first_level_tags->sectors->Protection",
    "first_level_tags->sectors->Shelter",
    "first_level_tags->sectors->Wash"
]

PILLARS_1D_LST = [
    "first_level_tags->pillars_1d->Casualties",
    "first_level_tags->pillars_1d->Context",
    "first_level_tags->pillars_1d->Covid-19",
    "first_level_tags->pillars_1d->Displacement",
    "first_level_tags->pillars_1d->Humanitarian access",
    "first_level_tags->pillars_1d->Information and communication",
    "first_level_tags->pillars_1d->Shock/event"
]

PILLARS_2D_LST = [
    "first_level_tags->pillars_2d->At risk",
    "first_level_tags->pillars_2d->Capacities & response",
    "first_level_tags->pillars_2d->Humanitarian conditions",
    "first_level_tags->pillars_2d->Impact",
    "first_level_tags->pillars_2d->Priority interventions",
    "first_level_tags->pillars_2d->Priority needs"
]

SUBPILLARS_1D_LST = [
    "subpillars_1d->Casualties->Dead",
    "subpillars_1d->Casualties->Injured",
    "subpillars_1d->Casualties->Missing",
    "subpillars_1d->Context->Demography",
    "subpillars_1d->Context->Economy",
    "subpillars_1d->Context->Environment",
    "subpillars_1d->Context->Legal & policy",
    "subpillars_1d->Context->Politics",
    "subpillars_1d->Context->Security & stability",
    "subpillars_1d->Context->Socio cultural",
    "subpillars_1d->Context->Technological",
    "subpillars_1d->Covid-19->Cases",
    "subpillars_1d->Covid-19->Contact tracing",
    "subpillars_1d->Covid-19->Deaths",
    "subpillars_1d->Covid-19->Hospitalization & care",
    "subpillars_1d->Covid-19->Prevention campaign",
    "subpillars_1d->Covid-19->Research and outlook",
    "subpillars_1d->Covid-19->Restriction measures",
    "subpillars_1d->Covid-19->Testing",
    "subpillars_1d->Covid-19->Vaccination",
    "subpillars_1d->Displacement->Intentions",
    "subpillars_1d->Displacement->Local integration",
    "subpillars_1d->Displacement->Pull factors",
    "subpillars_1d->Displacement->Push factors",
    "subpillars_1d->Displacement->Type/numbers/movements",
    "subpillars_1d->Humanitarian access->People facing humanitarian access constraints/humanitarian access gaps",
    "subpillars_1d->Humanitarian access->Physical constraints",
    "subpillars_1d->Humanitarian access->Population to relief",
    "subpillars_1d->Humanitarian access->Relief to population",
    "subpillars_1d->Humanitarian access->Security constraints",
    "subpillars_1d->Information and communication->Communication means and preferences",
    "subpillars_1d->Information and communication->Information challenges and barriers",
    "subpillars_1d->Information and communication->Knowledge and info gaps (hum)",
    "subpillars_1d->Information and communication->Knowledge and info gaps (pop)",
    "subpillars_1d->Shock/event->Hazard & threats",
    "subpillars_1d->Shock/event->Mitigating factors",
    "subpillars_1d->Shock/event->Type and characteristics",
    "subpillars_1d->Shock/event->Underlying/aggravating factors"
]

SUBPILLARS_2D_LST = [
    "subpillars_2d->At risk->Number of people at risk",
    "subpillars_2d->At risk->Risk and vulnerabilities",
    "subpillars_2d->Capacities & response->Humanitarian coordination",
    "subpillars_2d->Capacities & response->International response",
    "subpillars_2d->Capacities & response->Local response",
    "subpillars_2d->Capacities & response->National response",
    "subpillars_2d->Capacities & response->People reached/response gaps",
    "subpillars_2d->Capacities & response->Red cross/red crescent",
    "subpillars_2d->Humanitarian conditions->Coping mechanisms",
    "subpillars_2d->Humanitarian conditions->Living standards",
    "subpillars_2d->Humanitarian conditions->Number of people in need",
    "subpillars_2d->Humanitarian conditions->Physical and mental well being",
    "subpillars_2d->Impact->Driver/aggravating factors",
    "subpillars_2d->Impact->Impact on people",
    "subpillars_2d->Impact->Impact on systems, services and networks",
    "subpillars_2d->Impact->Number of people affected",
    "subpillars_2d->Priority interventions->Expressed by humanitarian staff",
    "subpillars_2d->Priority interventions->Expressed by population",
    "subpillars_2d->Priority needs->Expressed by humanitarian staff",
    "subpillars_2d->Priority needs->Expressed by population"
]

AGE_LST = [
    "secondary_tags->Age->12-17 years old",
    "secondary_tags->Age->18-24 years old",
    "secondary_tags->Age->18-59 years old",
    "secondary_tags->Age->25-59 years old",
    "secondary_tags->Age->5-11 years old",
    "secondary_tags->Age->5-17 years old",
    "secondary_tags->Age-><18 years",
    "secondary_tags->Age-><18 years old",
    "secondary_tags->Age-><5 years old",
    "secondary_tags->Age->>60 years old"
]

DISPLACED_LST = [
    "secondary_tags->Displaced->Asylum seekers",
    "secondary_tags->Displaced->Idp",
    "secondary_tags->Displaced->In transit",
    "secondary_tags->Displaced->Irregular",
    "secondary_tags->Displaced->Migrants",
    "secondary_tags->Displaced->Others of concern",
    "secondary_tags->Displaced->Pendular",
    "secondary_tags->Displaced->Refugees",
    "secondary_tags->Displaced->Regular",
    "secondary_tags->Displaced->Returnees",
    "secondary_tags->Displaced->Stateless"
]

GENDER_LST = [
    "secondary_tags->Gender->All",
    "secondary_tags->Gender->Female",
    "secondary_tags->Gender->Male"
]

NON_DISPLACED_LST = [
    "secondary_tags->Non displaced->Host",
    "secondary_tags->Non displaced->Non host"
]

SEVERITY_LST = [
    "secondary_tags->severity->Critical issue",
    "secondary_tags->severity->Issue of concern",
    "secondary_tags->severity->Minor issue",
    "secondary_tags->severity->No issue",
    "secondary_tags->severity->Severe issue"
]

SPECIFIC_NEEDS_GROUPS_LST = [
    "secondary_tags->specific_needs_groups->Child head of household",
    "secondary_tags->specific_needs_groups->Chronically ill",
    "secondary_tags->specific_needs_groups->Elderly head of household",
    "secondary_tags->specific_needs_groups->Female head of household",
    "secondary_tags->specific_needs_groups->Gbv survivors",
    "secondary_tags->specific_needs_groups->Indigenous people",
    "secondary_tags->specific_needs_groups->Lgbtqia+",
    "secondary_tags->specific_needs_groups->Minorities",
    "secondary_tags->specific_needs_groups->Persons with disability",
    "secondary_tags->specific_needs_groups->Pregnant or lactating women",
    "secondary_tags->specific_needs_groups->Single women (including widows)",
    "secondary_tags->specific_needs_groups->Unaccompanied or separated children",
    "secondary_tags->specific_needs_groups->Unaccompanied or/and separated children"
]

SUBSECTORS_LST = [
    "subsectors->Education->Facilities and amenities",
    "subsectors->Education->Learning environment",
    "subsectors->Education->Teachers and education personnel",
    "subsectors->Education->Teaching and learning",
    "subsectors->Health->Health care system",
    "subsectors->Health->Health status",
    "subsectors->Livelihoods->Assets",
    "subsectors->Livelihoods->Expenditures",
    "subsectors->Livelihoods->Income",
    "subsectors->Livelihoods->Skills and qualifications",
    "subsectors->Logistics->Communication",
    "subsectors->Logistics->Supply chain",
    "subsectors->Nutrition->Nutrition goods and services",
    "subsectors->Nutrition->Nutritional status",
    "subsectors->Protection->Child protection",
    "subsectors->Protection->Civil and political rights",
    "subsectors->Protection->Documentation",
    "subsectors->Protection->Freedom of movement",
    "subsectors->Protection->Housing land and property",
    "subsectors->Protection->Human rights",
    "subsectors->Protection->Justice and rule of law",
    "subsectors->Protection->Liberty",
    "subsectors->Protection->Mines",
    "subsectors->Protection->Physical safety and security",
    "subsectors->Protection->Sexual and gender based violence",
    "subsectors->Shelter->Domestic living space",
    "subsectors->Shelter->Dwelling enveloppe",
    "subsectors->Wash->Hygiene",
    "subsectors->Wash->Sanitation",
    "subsectors->Wash->Vector control",
    "subsectors->Wash->Waste management",
    "subsectors->Wash->Water supply"
]

AFFECTED_LST = [
    "first_level_tags->Affected->Displaced",
    "first_level_tags->Affected->Non displaced"
]
