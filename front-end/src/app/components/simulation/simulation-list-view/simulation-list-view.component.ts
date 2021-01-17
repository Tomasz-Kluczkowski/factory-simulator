import { Component, OnInit } from '@angular/core';
import {FactoryConfigAPIResource} from "../../../models/factory-config.models";
import {FactoryConfigService} from "../../../services/factory-config/factory-config.service";

@Component({
  selector: 'app-simulation-list-view',
  templateUrl: './simulation-list-view.component.html',
  styleUrls: ['./simulation-list-view.component.scss']
})
export class SimulationListViewComponent implements OnInit {
  factoryConfigs: FactoryConfigAPIResource[];


    constructor(private factoryConfigService: FactoryConfigService) {
  }

  ngOnInit(): void {
    this.factoryConfigService.list().subscribe(
      (data) => {
        this.factoryConfigs = data;
      }
    );
  }

}
