analysis_framework_q = """
SELECT
  *
FROM
  analysis_framework_analysisframework
"""

entries_q = """SELECT
  ee.*,
  pp.id as prj_id,
  pp.title
FROM
  entry_entry ee
  INNER JOIN project_project pp ON pp.id = ee.project_id
WHERE
  pp.id IN (
    '{}'
  ) and
  ee.created_at >= '{}'
order by ee.created_at asc
"""

af_widget_q = """SELECT
  *
FROM
  analysis_framework_widget
WHERE
  analysis_framework_id IN (
    SELECT
      DISTINCT ee.analysis_framework_id
    FROM
      entry_entry ee
      INNER JOIN analysis_framework_analysisframework af ON af.id = ee.analysis_framework_id
      INNER JOIN project_project pp ON pp.id = ee.project_id
    WHERE
      pp.id IN (
        '{}'
      )
  )
"""

exportdata_q = """SELECT
  *
FROM
  entry_exportdata
WHERE
  entry_exportdata.entry_id IN (
    SELECT
      ee.id
    FROM
      entry_entry ee
      INNER JOIN project_project pp ON pp.id = ee.project_id
    WHERE
      pp.id IN (
        '{}'
      )
  )
"""

af_exportables_q = """SELECT
  *
FROM
  analysis_framework_exportable
WHERE
  analysis_framework_id IN (
    SELECT
      DISTINCT ee.analysis_framework_id
    FROM
      entry_entry ee
      INNER JOIN analysis_framework_analysisframework af ON af.id = ee.analysis_framework_id
      INNER JOIN project_project pp ON pp.id = ee.project_id
    WHERE
      pp.id IN (
        '{}'
      )
  )
"""

projects_q = """SELECT
  *
FROM
  project_project pp
WHERE
  pp.id IN (
    '{}'
  )
  and pp.is_private=false
"""

new_projects_q = """
select pp.id, pp.status from project_project pp
    left join lead_lead ll
    on ll.project_id=pp.id
where pp.is_private=false
    and pp.is_deleted=false
group by pp.id
having count(ll.id) > 10
"""
# NOTE: having count(ll.id) > 10. 10 is experimental here. There are a lot of
# garbage projects with less than 10 leads. So this filter significantly
# reduces the number or projects to fetch.

lead_q = """SELECT
  ll.*,
  lp.text_extract text_extract,
  lp.word_count word_count,
  lp.page_count page_count
FROM
  lead_lead ll
LEFT JOIN lead_leadpreview lp on lp.lead_id = ll.id
WHERE
    ll.project_id={} and
    ll.created_at >= '{}'
order by ll.created_at asc
"""

entries_exportable_q = """
select * from (
    select distinct on (e.id)
        e.id,
        e.lead_id,
        e.information_date,
        exportable_id,
        entry_type,
        excerpt,
        excerpt_modified,
        ee.data export_data,
        ex.data af_exportable_data,
        e.created_at
    from entry_entry e
    inner join entry_exportdata ee on e.id = ee.entry_id
    inner join analysis_framework_exportable ex on ex.id = ee.exportable_id
    where e.project_id={} and
          e.created_at >= '{}'
  ) e
order by e.created_at asc
"""


af_q = """
select
    af.id,
    af.title,
    af.properties,
    af.description,
    af.created_at,
    array_agg(w.key) widget_keys,
    array_agg(w.widget_id) widget_ids,
    array_agg(w.title) widget_titles,
    array_agg(w.properties) widget_properties,
    array_agg(w.version) widget_versions
from analysis_framework_analysisframework af
inner join analysis_framework_widget w on w.analysis_framework_id=af.id
where
    af.is_private=false and
    af.created_at >= '{}'
group by af.id
order by af.id asc
"""

org_q = """
select
    o.*,
    ot.title organization_type
from organization_organization o
left join organization_organizationtype ot on ot.id=o.organization_type_id
where o.verified=true and
    o.created_at >= '{}'
order by o.created_at asc
"""
