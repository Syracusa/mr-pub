import van from "./van.js";
const { div, pre, ul, li } = van.tags;


const tests = [
    {
        name: 'Test1',
    },
    {
        name: 'Test2',
    },
    {
        name: 'Test3',
    },
    {
        name: 'Test4',
    },
];

const stages = [
    {
        name: 'Do A',
        detail: [
            'send a-1',
            'check a-1',
            'wait load',
        ]
    },
    {
        name: 'Do B',
        detail: [
            'send a-1',
            'check a-1',
            'wait load',
        ]
    },
    {
        name: 'Do C',
        detail: [
            'send a-1',
            'check a-1',
            'wait load',
        ]
    },
    {
        name: 'Do D',
        detail: [
            'send a-1',
            'check a-1',
            'wait load',
        ]
    }
];

const currStageIdx = 2;

const anomalies = [
    'Center frequency should be 10GHz(reported: 7GHz)',
    'Bandwidth should be 20MHz(reported: 10MHz)',
];

const Stage = (stage, stageIdx) => {
    if (stageIdx < currStageIdx)
        return div(
            ' - ' + stage.name, ' ✓',
            div(
                stage.detail.map(step => {
                    return pre('    - ' + step);
                })
            )
        );
    else
        return div(' - ' + stage.name);
}

const StageCont = (stages) => {
    return div(
        { class: 'stage-cont' },
        stages.map((stage, stageIdx) => {
            return () => Stage(stage, stageIdx);
        })
    );
}

const AnomalyCont = (anomalies => {
    return div(
        { class: 'anomaly-cont' },
        anomalies.map((anomaly) => {
            return div(anomaly);
        })
    );
});


const debugMsgs = [
    'Configuration xxxxx sent',
    'SW A Connected',
];

const DebugCont = ((dmsgs) => div(
    { class: 'debug-cont' },
    dmsgs.map(msg => div(msg))

));

const MainCont = () => {
    return (
        div(
            {
                class: 'main-cont'
            },
            div(
                {
                    style: () => 'display: flex; ',
                },
                div(
                    {
                        class: 'left-cont'
                    },
                    'Stages',
                    StageCont(stages),
                ),
                div(
                    {
                        class: 'right-cont'
                    },
                    'Anomaly',
                    AnomalyCont(anomalies),
                ),
            ),
            div(
                {
                    class: 'bottom-cont',
                },
                div(
                    {},
                    'Debug',
                    DebugCont(debugMsgs),
                ),
            ),

        ));
}

van.add(document.body, MainCont);