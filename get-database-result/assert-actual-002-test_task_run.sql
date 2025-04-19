SELECT 
    test_task_run_seq,test_result_seq,test_id,test_group,test_pipeline,test_task,simulation_date,start_time,end_time,test_result,evidence_link 
FROM 
    test_task_run 
ORDER BY
    test_task_run_seq
