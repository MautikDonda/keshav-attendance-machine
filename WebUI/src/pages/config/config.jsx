import { Button, DatePicker, Space, Input, Select } from "antd";
import {
  FileExcelOutlined,
  UserAddOutlined,
  EditOutlined,
  DeleteOutlined,
} from "@ant-design/icons";
import { useRef, useState } from "react";
import { CenteredLineText } from "../../components/CenteredLineText";
import "./config.css";
import TextArea from "antd/es/input/TextArea";

export const Config = () => {
  const [fromDate, setFromDate] = useState();
  const [toDate, setToDate] = useState();
  const [sabhaMode, setSabhaMode] = useState();
  const [syncUpMode, setSyncUpMOde] = useState();

  const rollNo = useRef();
  const rfidNo = useRef();
  const noOfRecords = useRef();
  const curlUrl = useRef();

  const modeOptions = [
    {
      value: "Sabha",
      label: "Sabha",
    },
    {
      value: "Dining",
      label: "Dining",
    },
    {
      value: "GetIn",
      label: "Get In",
    },
    {
      value: "GetOut",
      label: "Get Out",
    },
  ];

  const syncUpOptions = [
    {
      value: "Live Swipe",
      label: "LiveSwipe",
    },
    {
      label: "Server Time",
      value: "ServerTime",
    },
    {
      label: "Attendance Sync Up",
      value: "AttendanceSyncUp",
    },
    {
      label: "Users Sync Up",
      value: "UsersSyncUp",
    },
  ];

  const downloadAttendance = () => {
    //API Call
    console.log(fromDate + toDate);
  };

  const registerUser = () => {
    console.log(rollNo.current.input.value + " " + rfidNo.current.input.valuet);
  };

  const updateNoOfRecords = () => {
    console.log(noOfRecords.current.input.value);
  };

  const handleModeChange = (value) => {
    console.log(`selected mode ${value}`);
    setSabhaMode(value);
  };

  const handleSyncupChange = (value) => {
    setSyncUpMOde(value);
  };

  const handleFromDateChange = (_, dateString) => {
    setFromDate(dateString + "T00:00:00");
  };

  const handleToDateChange = (date, dateString) => {
    setToDate(dateString + "T00:00:00");
  };

  const updateCurrentMode = () => {
    //API Call
    console.log(sabhaMode);
  };

  const updateCurlOfOperation = () => {
    //API Call
    console.log(sabhaMode + " " + curlUrl.current.input.value);
  };

  const cleanUpLocalData = () => {
    //
  };

  return (
    <div className="center-align">
      <header>
        <h2 className="orange-color">WebUI For RFID Machine Configuration</h2>
      </header>
      <div className="main-layout">
        <section className="layout-container">
          <CenteredLineText text="Attendance" />
          <Space direction="vertical">
            <DatePicker
              onChange={handleFromDateChange}
              placeholder="Select from date"
            />
            <DatePicker
              onChange={handleToDateChange}
              placeholder="Select to date"
            />
            <Button
              className="raised-button"
              icon={<FileExcelOutlined />}
              onClick={downloadAttendance}
            >
              Download Attendance
            </Button>
          </Space>
          <CenteredLineText text="ID Registration" />
          <Space direction="vertical">
            <Input placeholder="Roll no." ref={rollNo} size="large" />
            <Input placeholder="RFID card no." ref={rfidNo} size="large" />
            <Button
              className="raised-button"
              icon={<UserAddOutlined />}
              onClick={registerUser}
            >
              Register
            </Button>
          </Space>
          <CenteredLineText text="Storage" />
          <h4 className="orange-color">Limit no of local records</h4>
          <Space direction="vertical">
            <Input placeholder="No. of records" ref={noOfRecords}></Input>
            <Button
              className="raised-button"
              icon={<EditOutlined />}
              onClick={updateNoOfRecords}
            >
              Update
            </Button>
          </Space>
          <CenteredLineText text="Cleanup" />
          <Button
            className="raised-button cleanup-button"
            icon={<DeleteOutlined />}
            onClick={cleanUpLocalData}
          >
            Clean up local data
          </Button>
        </section>
        <section className="layout-container">
          <CenteredLineText text="System" />
          <Space direction="vertical">
            <Select
              mode={sabhaMode}
              placeholder="Select mode"
              onChange={handleModeChange}
              options={modeOptions}
            />
            <Button
              className="raised-button"
              icon={<EditOutlined />}
              onClick={updateCurrentMode}
            >
              Update
            </Button>
          </Space>
        </section>
        <section className="layout-container">
          <CenteredLineText text="Sync Up" />
          <Space direction="vertical">
            <Select
              mode={syncUpMode}
              placeholder="Select sync up operation"
              onChange={handleSyncupChange}
              options={syncUpOptions}
            />
            <TextArea rows={4} ref={curlUrl} />
            <Button
              className="raised-button"
              icon={<EditOutlined />}
              onClick={updateCurlOfOperation}
            >
              Update
            </Button>
          </Space>
        </section>
      </div>
    </div>
  );
};
