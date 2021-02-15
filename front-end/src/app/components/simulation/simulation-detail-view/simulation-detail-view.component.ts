import {Component, Input, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-simulation-detail-view',
  templateUrl: './simulation-detail-view.component.html',
  styleUrls: ['./simulation-detail-view.component.scss']
})
export class SimulationDetailViewComponent implements OnInit {

  constructor(private route: ActivatedRoute) { }

  @Input('simulation')

  ngOnInit(): void {
  }

}
