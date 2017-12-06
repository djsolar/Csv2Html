#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FileName    : MainFrame
# Description : 
# @Date       : 2017/12/6
# @Time       : 12:42
# @Author     : zhouyiran
import wx
import os
from Main import transfer_csv_html


class MyFrame1(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"csv转", pos=wx.DefaultPosition,
		                  size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
		self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
		self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

		bSizer1 = wx.BoxSizer(wx.VERTICAL)

		self.m_filePicker1 = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"选择一个csv文件", u"*.csv",
		                                       wx.DefaultPosition, wx.Size(300, -1), wx.FLP_DEFAULT_STYLE)
		bSizer1.Add(self.m_filePicker1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

		self.m_button1 = wx.Button(self, wx.ID_ANY, u"转换html", wx.DefaultPosition, wx.DefaultSize, 0)
		self.Bind(wx.EVT_BUTTON, self.transferCsv2Html, self.m_button1)
		bSizer1.Add(self.m_button1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.SetSizer(bSizer1)
		self.Layout()

		self.Centre(wx.BOTH)

	def transferCsv2Html(self, event):
		path = self.m_filePicker1.GetPath()
		if os.path.exists(path):
			print 'path', path
			html_path = transfer_csv_html(path)
			dlg = wx.MessageDialog(None, u"生成文件成功：" + html_path, caption=u"提示",
			                 style=wx.OK)
			dlg.ShowModal()
		else:
			dlg = wx.MessageDialog(None, u"转换失败", caption=u"提示",
			                 style=wx.OK)
			dlg.ShowModal()

	def __del__(self):
		pass


class App(wx.App):  # 5 wx.App subclass
	"""Application class"""

	def OnInit(self):
		self.frame = MyFrame1(None)

		self.frame.Show(True)
		self.SetTopWindow(self.frame)
		return True


def main():
	app = App()
	app.MainLoop()


if __name__ == '__main__':
	main()
